# Git Commands & Workflow Guide

## 📋 Creating a Pull Request

### Step-by-Step Workflow

```bash
# 1. Create and switch to a feature branch
git checkout -b feature/name

# 2. Make your changes and commit
git add .
git commit -m "Your descriptive commit message"

# 3. Push your branch to GitHub
git push origin feature/name
```

### Then on GitHub:
1. Click the **"Compare & pull request"** button that appears
2. Add a descriptive title and description
3. Create the PR

---

## 🔀 Three Ways to Merge a Pull Request

### **1. Merge Pull Request (Regular Merge)**

Creates a **merge commit** that combines your branch with main while preserving all commit history.

**Example:**
```
Before:
main:    X ─── Y
feature:      A ─── B ─── C

After MERGE:
main:    X ─── Y ─── [Merge commit] ─── A ─── B ─── C
```

- **Git history:** Non-linear, shows exactly when the branch was merged
- **All commits preserved:** Yes
- **Merge commit created:** Yes
- **Use when:** You want to preserve the complete development history and track integration points

---

### **2. Squash and Merge**

Combines **all commits from your branch into ONE single commit** before merging to main.

**Example:**
```
Before:
main:    X ─── Y
feature:      A ─── B ─── C

After SQUASH & MERGE:
main:    X ─── Y ─── [1 NEW COMMIT: A+B+C combined]
```

- **Git history:** Linear and clean
- **All commits preserved:** No (combined into 1)
- **Merge commit created:** No
- **Use when:** You want a clean history and don't care about individual intermediate commits from feature development

**Best for:** Simple features, bug fixes, or when commit history during development isn't important

---

### **3. Rebase and Merge**

**Replays each commit from your branch** on top of main, then fast-forwards main. No merge commit is created.

**Example:**
```
Before:
main:    X ─── Y
feature:      A ─── B ─── C

After REBASE & MERGE:
main:    X ─── Y ─── A ─── B ─── C
```

- **Git history:** Linear and clean
- **All commits preserved:** Yes (individually)
- **Merge commit created:** No
- **Use when:** You want a clean linear history AND want to preserve individual commit messages

**Best for:** Maintaining detailed history while keeping the main branch timeline linear

---

## 📊 Comparison Table

| Strategy | History Shape | Number of Commits | Merge Commit | Best Use Case |
|----------|---------------|-------------------|--------------|---------------|
| **Merge** | Non-linear | All preserved | ✅ Yes | Large features, tracking merge points |
| **Squash** | Linear | 1 combined | ❌ No | Simple features, clean history |
| **Rebase** | Linear | All individual | ❌ No | Detailed history + clean timeline |

---

## 💡 Team Best Practices

- **Squash and Merge:** Most commonly used for cleaner main branch history
- **Rebase and Merge:** Used when detailed commit history is important
- **Regular Merge:** Used in complex projects where tracking merge points matters

---

## 🔍 Viewing Changes Before Committing

```bash
# See all modified files
git status

# See what changed in files
git diff

# See staged changes ready to commit
git diff --staged

# Compare your branch with main before pushing
git diff main..your-branch-name
```

---

## 📝 Useful Git Commands

```bash
# View commit history
git log

# See commits in your branch not in main
git log main..HEAD

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (discard changes)
git reset --hard HEAD~1

# Switch branches
git checkout branch-name

# List all branches
git branch -a

# Delete a branch locally
git branch -d branch-name

# Delete a branch on GitHub
git push origin --delete branch-name
```
