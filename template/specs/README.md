# Specifications Directory

**Purpose**: Living documentation for technical and business decisions.

## Structure

### Root `specs/` Directory
Cross-cutting concerns that affect the entire project:
- **devops-infrastructure.md** - Deployment, logging, database, CI/CD decisions
- Future: authentication.md, api-conventions.md, security-policies.md

### App-Specific `specs/`
Each Django app can have its own `specs/` subdirectory:
- `django_starter/apps/<app_name>/specs/`
  - `models.md` - Data model decisions and relationships
  - `business-rules.md` - Domain logic and validation rules
  - `integrations.md` - External service integrations
  - `api.md` - API design for endpoints exposed by this app

## When to Create/Update Spec Files

### Create a new spec when:
- Making an architectural decision that affects multiple files
- Choosing between multiple technical approaches
- Documenting business rules that aren't obvious from code
- Establishing conventions for the team to follow

### Update existing specs when:
- Decisions change or evolve
- New context makes previous rationale obsolete
- Implementation reveals insights not captured initially
- Adding examples or patterns based on real usage

### Avoid creating specs for:
- Implementation details that belong in code comments
- Temporary decisions or experiments
- Information already well-documented in official library docs
- Obvious conventions (follow existing patterns)

## Spec File Template

```markdown
# [Topic Name]

**Purpose**: Brief description of what decisions this spec covers.

**Last Updated**: YYYY-MM-DD

---

## [Decision 1]

**Decision**: Clear statement of what was decided.

**Rationale**:
- Why this choice was made
- Trade-offs considered

**Alternatives Considered**:
- Option 1: Why not chosen
- Option 2: Why not chosen

**Status**: Implemented / In Progress / [Pending]

---

## [Decision 2]

...
```

## Guidelines for AI Assistants

When making architectural decisions:
1. **Check specs first** - Review relevant spec files before proposing solutions
2. **Reference in discussions** - Link to specs when explaining rationale
3. **Update after changes** - Keep specs synchronized with implementation
4. **Ask before creating** - Suggest new spec files but get user confirmation
5. **Keep concise** - Specs are decision records, not tutorials

## Guidelines for Developers

- Specs are **living documents** - update them when reality diverges
- **Link to specs** in code comments when implementing complex decisions
- **Reference specs** in PR descriptions to provide context
- Keep specs **concise and scannable** - developers will read them
- Prefer **tables and bullet points** over long paragraphs
- Use mermaid diagrams to illustrate different flows

## Cross-Referencing

Link between specs using relative paths, the specs/ folder at the root of the project


