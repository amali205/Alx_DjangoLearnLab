
---

## 📄 5. `CRUD_operations.md` (Full Summary)

```markdown
# 📘 Full CRUD Operations in Django Shell

---

## 🟢 Create

```python
from bookshelf.models import Book

book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(book)
# Output: <Book: 1984 by George Orwell (1949)>
