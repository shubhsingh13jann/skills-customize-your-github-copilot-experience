---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---
## Assignment Markdown Structure Guidelines

All assignment markdown files must follow the repository template and the conventions below so students see a consistent, clear experience.

### Template & filename

- **Template**: Base every assignment on [`templates/assignment-template.md`](../../templates/assignment-template.md).
- **Filename/location**: Each assignment's primary markdown must be `README.md` placed in the assignment folder (for example: `assignments/python-basics/README.md`).
- **Keep sections**: Do not remove or rename required template sections or emojis/icons.

### Required sections and content

- **Title**: Use the exact header format from the template (include the 📘 emoji). Keep the title short and descriptive.
- **Objective**: 1–2 sentences describing the learning goal.
- **Tasks**: For each task use the template's `🛠️` task headings and include the following subsections:
   - **Description**: Clear, actionable instructions for the student.
   - **Requirements**: Bullet-list of measurable acceptance criteria (what the program must do).
   - **Examples**: Add example input/output where helpful using fenced code blocks with the correct language (e.g., ```python).

### Additional conventions

- **Starter code & assets**: Reference starter files with relative paths (e.g., `starter-code.py`, `data.csv`) and keep those files inside the assignment folder.
- **Code blocks**: Always specify the language for syntax highlighting (```python, ```bash, etc.).
- **Short and scannable**: Keep each task focused — prefer many small tasks over one large ambiguous task.
- **Accessibility & clarity**: Use plain language, short sentences, and avoid unnecessary jargon.

### Quick checklist for authors

- Copy `templates/assignment-template.md` into `assignments/<assignment>/README.md`.
- Ensure emojis and headers match the template.
- Add relative links to any `starter-code` or `data` files inside the same folder.
- Verify code fences include a language tag.
- Run a quick read for clarity and measurable Requirements.

If you need help applying the template to an existing assignment, open an issue or ask for a review.