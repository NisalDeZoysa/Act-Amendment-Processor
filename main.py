from src.tracker import AmendmentTracker

if __name__ == "__main__":
    base_pdf = "data/14-2010_E.pdf"
    amendments = ["data/24-2023_E.pdf"]

    tracker = AmendmentTracker(base_pdf, amendments)
    all_changes = tracker.run()

    print("\n=== Extracted Changes ===")
    for change in all_changes:
        print(f"Section {change['section']}({change['subsection']})[{change['clause']}] → {change['change_type']}")
