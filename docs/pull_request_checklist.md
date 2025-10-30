# ✅ Pull Request Checklist

Before creating a PR (Pull Request), make sure you’ve done the following:

1. **Code Quality**
- [ ] Code runs without errors.
- [ ] No unnecessary print/debug statements.
- [ ] Follows project naming and folder conventions.

2. **Testing**
- [ ] Tested locally for functionality.
- [ ] No breaking changes introduced.
- [ ] Database connections and data files work correctly.

3. **Documentation**
- [ ] README or doc updated (if feature affects setup or usage).
- [ ] Added comments where logic may be unclear.
- [ ] Linked related issue (if applicable).

4. **Git Hygiene**
- [ ] Proper commit messages used.
- [ ] Branch is up to date with `main`.
- [ ] Conflicts resolved before merge.

---

 **Final Step Before Merge**
- Get at least one peer review (if team project).
- Run `git pull origin main` to ensure your branch is clean.
- Confirm no unwanted files (`venv`, `data/raw`, etc.) are committed.
