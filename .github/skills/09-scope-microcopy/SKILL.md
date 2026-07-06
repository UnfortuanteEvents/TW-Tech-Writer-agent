---
name: 09-scope-microcopy
description: 'Task 9 of the Tech Writer workflow. Use to analyze UI changes for a Cin7 Jira issue and populate microcopy requirements (Location, Element, Current, Notes) into the Microcopy working Google Sheet, plus a summary in the issue description.'
argument-hint: 'Jira issue ID'
---

# Task 9 — Scope microcopy

Gather and analyze available resources to define the microcopy requirements for the issue.

## Discovery

Collect relevant materials from the following sources only:

- The issue, its parent, its children, and any issues linked to any of those
- External files (e.g. Figma designs, Confluence pages, Google Drive docs) that are
  explicitly referenced in or attached to one of the above issues

When evaluating the available sources, prefer in this order:

1. **Ideal:** Figma designs, Claude mock-ups, or interactive prototypes
2. **Acceptable:** Screenshots or written explanation of the UI changes

If only a written explanation is available, note this in the microcopy summary added to
the issue description.

Do not browse third-party apps independently to find additional resources.

## Analysis

Using the gathered resources and the product model for the relevant product (Core or Omni),
identify microcopy requirements by examining the UI changes involved. Use the product
model's navigation architecture to anchor each affected page to its level-1 and level-2
location before drilling down to the specific page or section.

Categorize affected pages as follows:

- **Updated pages** — existing app pages (including modals and dialogs) that have
  microcopy requirements (new, updated, or deleted microcopy)
- **New pages** — new app pages (including modals and dialogs) where all microcopy will be
  new or migrated from an existing page
- **Deleted pages** — existing app pages (including modals and dialogs) that will be
  removed (microcopy will be deleted or migrated to another page)

For each updated or new page, apply the following template — repeat it unchanged for every
page; do not vary the structure:

> **Page:** [level-1 > level-2 > page name, from the product model — e.g. `Sales > Sales Orders > Filters panel`]
> - **New microcopy needed:** [describe each item, or "None"]
> - **Existing microcopy to update:** [describe each item, or "None"]
> - **Existing microcopy to delete:** [describe each item, or "None"]

For deleted pages, note each one separately and record what happens to its microcopy
(deleted or migrated to another page).

## Output

Add the microcopy requirements to the Microcopy working file (Google Sheet) linked in the
issue's **Working files** section. Populate one row per microcopy item using the sheet's
seven columns:

| Column | Content | Who populates |
|---|---|---|
| Location | The app page or area where the microcopy appears | Agent |
| Element | The specific UI element (e.g. button label, tooltip, field placeholder) | Agent |
| Current | The existing text if you are confident of it; `UNKNOWN` if you are unsure; `NEW` if the element is new and has no existing microcopy | Agent |
| New | Leave blank for now (populated in Task 13) | Agent (leave blank) |
| Notes | Any additional context, such as whether the item is new, updated, or deleted | Agent |
| Questions/Comments | Feedback or open questions for Product/Design (optional; typically completed after Task 13) | Manual |
| QA | QA sign-off or review status (optional; typically completed post-draft) | Manual |

Populate Location, Element, Current, and Notes columns only; leave New,
Questions/Comments, and QA blank.

Group rows by page, adding a blank row between each page's items for readability. Include a
row for each microcopy item on pages being deleted, leaving **Current** as "DELETE",
**New** blank, and noting why in the **Notes** column.

For dialogs/modals, use a single row per dialog/modal and represent the text in plain text
segments separated by `|` in this order: Heading | Body | CTA 1 | CTA 2 (add more CTA
segments if needed).

Also add a brief summary of the microcopy requirements to the issue description, organized
by page.
