# Contribution Workflow Guide 📂

This guide explains the **recommended workflow for contributing teaching content** to the `python-textutils` repository.

The goal is to keep the repository **structured, consistent, and easy to understand** for learners exploring Python import mechanics and packaging fundamentals.

---

## 🎯 When Should You Follow This Guide?

Follow this workflow when:
- You are explaining a **new concept**
- The explanation requires **code examples**
- You are adding a **walkthrough-style contribution**

For small fixes (typos, minor wording changes), this workflow is optional.

---

## 📁 Step 1: Create a Dedicated Concept Folder

For every new concept, create a folder at the **repository root** named after the concept.

### Folder Naming Rules
- Use lowercase letters
- Use hyphens (`-`) instead of spaces
- Keep names descriptive and short

### Examples

  ```bash
    absolute-vs-relative-imports/
    sys-path-behavior/
    circular-imports/
    init-py-explained/
  ```

---

## 📘 Step 2: Add a README.md (Mandatory)

Each concept folder **must include a `README.md`** explaining:

- What the concept is
- Why it matters
- How Python behaves in this scenario
- Common mistakes or misconceptions
- How the included code demonstrates the concept

Write explanations in a **step-by-step and beginner-friendly** manner.

---

## 🧪 Step 3: Add Python Code Examples

Add `.py` files to demonstrate the concept in action.

### Guidelines
- Keep examples small and focused
- Use meaningful file names
- Add comments explaining *why* behavior occurs
- Avoid unnecessary abstractions

### Example Structure

```bash
absolute-vs-relative-imports/
├── README.md
├── main.py
├── module_a.py
└── module_b.py
```

---

## ▶️ Step 4: Make Examples Runnable

All examples should:
- Run using standard Python commands (`python file.py`)
- Avoid external dependencies unless required
- Mention execution instructions inside the README

---

## 🧠 Step 5: Teach, Don’t Just Show

When contributing:
- Prefer clarity over clever tricks
- Explain unexpected or confusing behavior explicitly
- Assume the reader is learning Python internals

---

## 🔄 Step 6: Updating Existing Concepts

If modifying an existing concept:
- Update both **documentation and code**
- Ensure examples still match explanations
- Avoid behavior changes without explanation

---

## ✅ Summary

**Good contributions:**
- One concept → one folder
- Clear README + runnable examples
- Simple explanations with real behavior

This workflow keeps `python-textutils` easy to navigate and scalable as more concepts are added.

Happy contributing! 🚀

---

