
---

## 📄 4. `delete.md`

```markdown
# ✅ Delete Book Instance

```python
from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm Deletion
print(Book.objects.all())
