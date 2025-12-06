# esper_thesis/cli.py

import argparse
from pathlib import Path
from typing import List

from dataclasses import asdict

from .config import __version__, get_database_path
from .model import ResearchPacket, ResearchType
from .processor import process_research_item
from .storage import load_database, save_database
from .export import export_json, export_markdown


def cmd_create(args, packets: List[ResearchPacket], db_path: Path) -> None:
    """Create new research packet."""
    packet = process_research_item(
        title=args.title,
        abstract=args.abstract,
        key_findings=args.findings,
        research_type=ResearchType(args.type),
        source=args.source,
        methodology=args.methodology or "",
        existing_packets=[asdict(p) for p in packets],
        tags=args.tags or [],
    )
    packets.append(packet)
    save_database(packets, db_path)
    print(f"✓ Created packet {packet.packet_id} ({packet.title})")
    print(f"  Database: {db_path}")


def cmd_list(args, packets: List[ResearchPacket], db_path: Path) -> None:
    """List research packets."""
    filtered = packets
    if args.type:
        rtype = ResearchType(args.type)
        filtered = [p for p in filtered if p.research_type == rtype]

    if args.sort == "priority":
        filtered = sorted(filtered, key=lambda p: p.priority_score, reverse=True)
    else:
        filtered = sorted(filtered, key=lambda p: p.timestamp, reverse=True)

    if args.limit:
        filtered = filtered[: args.limit]

    print(f"Database: {db_path} ({len(packets)} packets total)")
    for p in filtered:
        rt = p.research_type.value
        rd = p.routing_decision.value if p.routing_decision else "unrouted"
        print(
            f"- [{rt}] {p.title}  "
            f"(priority={p.priority_score:.2f}, routing={rd}, id={p.packet_id})"
        )


def cmd_stats(args, packets: List[ResearchPacket], db_path: Path) -> None:
    """Print corpus statistics."""
    print(f"Database: {db_path}")
    print(f"Total packets: {len(packets)}")
    if not packets:
        return

    by_type = {}
    for p in packets:
        by_type.setdefault(p.research_type.value, 0)
        by_type[p.research_type.value] += 1

    print("\nBy Type:")
    for t, count in sorted(by_type.items()):
        print(f"  {t}: {count}")

    avg_priority = sum(p.priority_score for p in packets) / len(packets)
    print(f"\nAverage Priority: {avg_priority:.2f}")


def cmd_export(args, packets: List[ResearchPacket], db_path: Path) -> None:
    """Export research findings."""
    output_path = Path(args.output) if args.output else None

    if args.format == "json":
        if output_path is None:
            # default json export path
            output_path = Path("research.json")
        export_json(packets, output_path)
        print(f"✓ Exported {len(packets)} packets to JSON → {output_path}")

    elif args.format == "markdown":
        export_markdown(packets, output_path)
        if output_path:
            print(f"✓ Exported {len(packets)} packets to Markdown → {output_path}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="ESPER-THESIS: Research Management System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--database",
        help="Path to research database JSON (overrides env/config)",
    )
    parser.add_argument(
        "--project",
        help="Named project key from ~/.esper_thesis/config.json",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"ESPER-THESIS {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    # create
    create_p = subparsers.add_parser("create", help="Create a new research packet")
    create_p.add_argument("--title", required=True)
    create_p.add_argument(
        "--type",
        required=True,
        choices=[t.value for t in ResearchType],
    )
    create_p.add_argument("--abstract", required=True)
    create_p.add_argument("--findings", nargs="+", required=True)
    create_p.add_argument("--source", default="manual")
    create_p.add_argument("--methodology", default="")
    create_p.add_argument("--tags", nargs="*")

    # list
    list_p = subparsers.add_parser("list", help="List research packets")
    list_p.add_argument("--type", choices=[t.value for t in ResearchType])
    list_p.add_argument(
        "--sort",
        choices=["priority", "date"],
        default="priority",
    )
    list_p.add_argument("--limit", type=int, default=20)

    # stats
    subparsers.add_parser("stats", help="Show statistics for the database")

    # export
    export_p = subparsers.add_parser("export", help="Export findings")
    export_p.add_argument(
        "--format",
        choices=["json", "markdown"],
        default="json",
    )
    export_p.add_argument("--output", help="Output file path")

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    db_path = get_database_path(args)
    packets = load_database(db_path)

    if args.command == "create":
        cmd_create(args, packets, db_path)
    elif args.command == "list":
        cmd_list(args, packets, db_path)
    elif args.command == "stats":
        cmd_stats(args, packets, db_path)
    elif args.command == "export":
        cmd_export(args, packets, db_path)
