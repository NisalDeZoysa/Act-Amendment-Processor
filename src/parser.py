import re

class AmendmentParser:
    @staticmethod
    def detect_amendments(base_text: str, amendment_text: str):
        """
        Finds amended sections and extracts the changes.
        Supports 'substitution', 'repeal', 'insert', etc.
        """
        amendments = []

        # Pattern: Section X amended in subsection (Y) by substitution of paragraph (Z)
        pattern = r"Section (\d+).*?amended.*?subsection \((\d+)\).*?paragraph \(([a-z])\).*?(substitution|repeal|insert).*?:-(.*?)\."
        matches = re.findall(pattern, amendment_text, flags=re.DOTALL | re.IGNORECASE)

        for match in matches:
            section, subsection, clause, change_type, new_text = match

            # Find the old text from the base act for reference
            base_pattern = rf"Section {section}.*?subsection \({subsection}\).*?paragraph \({clause}\)(.*?)(?=\([a-z]\)|\n\n|\Z)"
            old_match = re.search(base_pattern, base_text, flags=re.DOTALL | re.IGNORECASE)
            old_text = old_match.group(1).strip() if old_match else None

            amendments.append({
                "section": int(section),
                "subsection": int(subsection),
                "clause": clause,
                "change_type": change_type.lower(),
                "old_text": old_text,
                "new_text": new_text.strip()
            })

        return amendments
