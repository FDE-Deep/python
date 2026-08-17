# 🐍 Python Learning Log — JS/TS Developer → AI Engineer

A running record of my Python learning journey. Background: 7 years as a JavaScript/TypeScript
developer, now learning Python from scratch with the goal of becoming an AI engineer.

**Approach:** understand the _why_, not just the syntax · predict outputs before running ·
explain concepts back in my own words · consolidate each cluster with a real project.

---

## 📊 Progress at a glance

| Cluster                                                             | Status                        |
| ------------------------------------------------------------------- | ----------------------------- |
| Core data structures (list/tuple/set/dict, Big-O)                   | ✅ Done                       |
| Comprehensions (list/dict/set) + `zip`                              | ✅ Done                       |
| Iterators & generators (`yield`, laziness)                          | ✅ Done                       |
| Functions deep (`*args`/`**kwargs`, closures, mutable-default trap) | ✅ Done                       |
| OOP — classes, dunders, dataclasses                                 | ✅ Done                       |
| OOP — inheritance, `super()`, composition                           | ✅ Done                       |
| OOP — polymorphism & duck typing                                    | ✅ Done                       |
| OOP — method overloading (why Python skips it)                      | ✅ Done                       |
| OOP — method types (`@classmethod`, `@staticmethod`, factories)     | ✅ Done                       |
| OOP — encapsulation & `@property`                                   | ✅ Done                       |
| OOP — abstraction (abstract base classes)                           | ✅ Done                       |
| OOP — multiple inheritance, MRO, mixins                             | ✅ Done                       |
| **OOP cluster**                                                     | ✅ **Complete**               |
| OOP — `__str__` vs `__repr__`                                       | ⬜ Skipped (revisit optional) |
| Exception handling                                                  | ⬜ Next                       |
| Decorators                                                          | ⬜ Planned                    |

**Projects built:** Word Frequency Analyzer (streaming CLI tool) ✅ · Library Management System ⬜ (OOP consolidation — upcoming)

---

## 🗂️ Topics covered — reference

### 1. Core data structures

- **list, tuple, set, dict** — when to use each
- **Big-O** of get / insert / search → the _array vs hash table_ insight
  (list membership `in` is O(n); dict/set lookup is O(1) via hashing)
- **List copying:** `.copy()`, `list()`, slice `[:]` — all shallow; `copy.deepcopy()` for nested
- **Joining lists:** `+` (new list) vs `append` (one item, in place) vs `extend` (many, in place);
  never `+` in a loop (O(n²))
- **Dict views:** `.keys()`, `.values()`, `.items()` are _live_ views; `list(view)` to freeze
- **Nested dict iteration**; `tuple(d)` gives keys only (gotcha)

### 2. Comprehensions

- **List:** `[expr for x in it if cond]`; `if/else` goes _before_ `for` (expression position)
- **Dict:** `{k: v for ...}` — with `zip`, `.items()`, filtering, inverting
- **Set:** `{expr for ...}` — dedupes; `{}` is an empty _dict_, not a set
- **Nested:** two `for` clauses, read left-to-right as stacked loops
- **`zip`:** pairs iterables into tuples, lazy, stops at shortest; `zip(*pairs)` unzips
- **Judgment:** comprehensions do _map + filter_, **not** _reduce_ (use a loop or `collections.Counter`)

### 3. Iterators & generators

- **iterable vs iterator:** iterable = reusable source; iterator = single-use _worker_
- **`iter()` / `next()` / `StopIteration`** — the machinery a `for` loop hides
- **Exhaustion:** iterators are single-use; a generator returns _itself_ from `iter()`
- **`yield`:** _pauses_ the function (freezes the frame), resumes on next `next()`
- **Generator expressions:** `(expr for x in it)` — lazy sibling of a list comp
- **Why it streams:** one item at a time; values don't exist until computed → constant memory
- **By-hand iterator:** `__iter__` + `__next__` on a class (what `yield` generates for you)

### 4. Functions deep

- **First-class functions:** `func` = the machine, `func()` = press "go"
- **`*args` / `**kwargs`:** *gather* in the def (`*`→tuple, `\*\*`→dict), *spread\* at the call
- **Closures:** inner function remembers variables captured **once at creation** (capture-time vs call-time)
- **Mutable-default trap:** `def f(x=[])` — default made once at definition, shared across calls;
  fix with `None` + create inside (or `field(default_factory=list)` in dataclasses)

### 5. OOP — foundations

- **Classes, `__init__`, `self`** — blueprint vs instance; `d.bark()` is really `Dog.bark(d)`
- **Instance vs class attributes** — per-object vs shared
- **Dunder methods:** `__repr__`, `__eq__`, `__add__`, `__len__` — built-ins map to dunder hooks
- **`@dataclass`** — auto `__init__`/`__repr__`/`__eq__`; `default_factory` for mutable defaults;
  `__post_init__` for extra init logic

### 6. OOP — inheritance & composition

- **Inheritance:** `class Child(Parent)`, method overriding, `super().__init__(...)`
  (needed only when the child _defines its own_ `__init__` but wants the parent's setup too)
- **Composition:** an object _holds_ other objects (`self.engine = engine`)
- **is-a → inheritance · has-a → composition;** favor composition (more flexible)

### 7. OOP — the four pillars

- **Polymorphism:** same method/operator name, many behaviors per type; one loop handles many types
- **Duck typing:** Python checks whether the _method exists_, not the _type_ ("if it quacks…");
  dunders are duck typing built into the language
- **Encapsulation:** control access to data. `@property` = method accessed like an attribute (no `()`);
  getter + `@x.setter` for validation; getter-only = read-only.
  **Python privacy is cooperative, not enforced** — `_name` is a convention (still reachable);
  `__name` triggers name-mangling (`_Class__name`) — a stronger speed bump, still not absolute.
  Routing through the property (even inside the class) enforces validation; direct `_field` access bypasses it.
- **Abstraction:** `class X(ABC)` + `@abstractmethod` = a contract subclasses **must** implement.
  Can't instantiate an abstract class, nor a subclass that skips a required method (error **at creation**).
  Enforces _existence_, not _usefulness_ (a `pass` body counts as "implemented").
  **Abstraction guarantees the interface; duck typing hopes for it.**

### 8. OOP — method types & overloading

- **instance method** (`self`) — needs a specific object's data
- **`@classmethod` (`cls`)** — needs the class; used for **factory methods** (`from_dict`, `from_csv_line`,
  `square`) and class-level state (`get_count`)
- **`@staticmethod`** — needs neither; a related utility grouped in the class
- **Factory pattern:** a `@classmethod` that builds & returns an instance from data in a different shape;
  build **one** from **one** record, use a comprehension / `from_list` for **many**
- **Method overloading:** Python _doesn't_ have it — a second `def` of the same name _replaces_ the first;
  use default args / `*args` / `isinstance` inside one method instead

### 9. OOP — multiple inheritance & MRO

- **Multiple inheritance:** `class D(B, C)` — combines methods from several parents
- **MRO (Method Resolution Order):** the search order for methods — **child first, parents left-to-right**,
  computed by **C3 linearization**; view with `.__mro__` (ends in `object`); first match wins
- **Diamond problem:** shared grandparent is checked _once, at the end_, after all intermediate parents
- **`super()` follows the MRO** — "next in MRO," not literally "my parent" → cooperative multi-parent init
  (each parent's `__init__` runs once)
- **Mixins:** small, single-purpose, non-overlapping capability classes (`LoggerMixin`, `JSONMixin`);
  the _good_ multiple inheritance — structured to **avoid** diamonds, not resolve them
- **Guidance:** use MI sparingly; prefer composition or focused mixins over deep diamonds

---

## 🛠️ Projects

### Word Frequency Analyzer ✅

A CLI tool that reads a text file and reports the most frequent words. **Streams** the file with a
generator, so it handles files larger than RAM.

- **Concepts:** generators + `yield`, `with open`, dicts + `.get()`, sorting with a `key`, `.items()`,
  comprehensions, module structure (`analyzer.py` / `main.py`), `if __name__ == "__main__"`
- **Bugs solved:** `return` closing the file before a lazy generator reads it (→ use `yield`);
  character-vs-word split; slicing a dict (→ sort into a list first)
- **Known limit:** line-based streaming assumes reasonably small lines (one giant line = loads it all)

### Library Management System ⬜ (upcoming — OOP consolidation)

Will tie together: dataclasses (`Book`/`Member`), an abstract `LibraryItem` base (abstraction),
composition (`Library` _has_ items/members), factories (`from_dict`), `@property` (controlled access),
polymorphism across item types, plus file I/O and dicts.

---

## 🧭 Cross-cutting principles internalized

- **References vs copies** — a name points to an object; `is` (identity) vs `==` (equality/value)
- **Reassignment vs mutation** — reassign rebinds a name (safe); mutating changes the shared object
  (leaks). Immutables (str/int/tuple) can _only_ be reassigned → always safe as defaults
- **Definition-time vs call-time / capture-time vs call-time** — defaults & closures fix values early
- **Loud failures beat silent ones** — raise/validate rather than silently returning wrong data
- **Let objects handle themselves** — ask an object (`x.describe()`), don't reach into its internals
- **Delegate, don't duplicate** — one source of truth (e.g. `from_list` reuses `from_dict`)
- **Meaningful naming** — never shadow built-ins (`list`, `dict`, `sum`, `str`)
- **Match structure/validation to need** — don't over-engineer; validate at boundaries
- **Predict output before running** — active reasoning over passive reading

### JS/TS → Python transition notes

- Comma makes a tuple, **not** the parentheses (`(5)` is `5`; `(5,)` is a tuple)
- Default params: **per-call fresh in JS**, but **evaluated once at definition in Python** (→ the trap)
- `this` → `self` (explicit first param); `new Dog()` → `Dog()`; `constructor` → `__init__`
- No `export` — every top-level name is importable; importing _runs_ the file (→ `__name__` guard)
- Type hints **not enforced at runtime** (like TS types — checked by a separate tool: Pylance/Pyright)
- `&&`/`||`/`!` → `and`/`or`/`not`; `null`/`undefined` → `None`; no `===` (use `==` / `is`)
- No method overloading; `private` isn't enforced (cooperative privacy via `_` / `__`)

---

## 🧰 Tooling & workflow

- **VS Code + Pylance** — `"python.analysis.typeCheckingMode": "basic"` (TS-style static checking)
- **Claude Code** extension installed in VS Code (in-editor AI assistant; use to _review/explain_, not to
  write the code I'm learning to write myself)
- **Git** — `init` / `add` / `commit` / `push`, `.gitignore` (`__pycache__/`, `venv/`, `.env`)
- **README / repo conventions** — one repo per project, one grouped repo for practice
- **LinkedIn** — documenting the journey publicly (posted about generators & the 2GB-file problem)

---

## 📅 Session log

> Newest entries at the top.

### Session — Encapsulation, abstraction, MRO (OOP cluster COMPLETE)

- **Covered:** encapsulation (`_`/`__`, `@property`, getters/setters, validation), abstraction
  (ABCs, `@abstractmethod`), multiple inheritance, MRO, C3 linearization, the diamond problem, mixins
- **Key insights:**
  - Python privacy is _cooperative, not enforced_ — `_balance` can be bypassed; `__` name-mangling is a
    stronger speed bump but still reachable via `_Class__name`. Real protection is social, not technical.
  - Abstraction enforces a method's _existence_, not its _usefulness_ — a `pass` body still satisfies the
    contract; only _not defining_ the method triggers the error. `@abstractmethod` marks a method
    "incomplete," so the class can't be instantiated until a subclass finishes it.
  - MRO: child → parents left-to-right → shared grandparent last (C3). `super()` = "next in MRO," not
    "parent" — enables cooperative multi-parent init. Mixins _avoid_ diamonds by being non-overlapping.
- **Predictions:** nailed every MRO including the diamond (`D → B → C → A → object`) on first pass.
- **Also:** set up Claude Code in VS Code; keep chat (tutor) + Claude Code (editor assistant) separate.
- **Revisit:** `__str__` vs `__repr__` (skipped — optional); then Library project, then exception handling.

### Session — OOP pillars & method types

- **Covered:** polymorphism, duck typing, method overloading (why Python lacks it),
  `@classmethod` / `@staticmethod`, factory pattern (`from_dict` / `from_list`)
- **Key insight:** Python resolves methods by _name at runtime_ and never checks argument types — it runs
  and fails only if an operation is genuinely impossible. Factories build _one_ from _one_ record;
  comprehensions/`from_list` handle _many_.

### Session — OOP foundations & inheritance

- **Covered:** classes, `__init__`, `self`, methods, dunders, `@dataclass`, inheritance, `super()`,
  composition, is-a vs has-a
- **Deep detours:** mutability/references through strings, lists, functions & dataclasses; JS mapping;
  `default_factory` = the mutable-default trap, caught by dataclass

### Session — Functions deep

- **Covered:** first-class functions, `*args`/`**kwargs`, closures (capture-time), mutable-default trap

### Session — Iterators & generators (+ Word Analyzer project)

- **Covered:** iterables vs iterators, `iter`/`next`/`StopIteration`, exhaustion, `yield`, generator
  expressions, why generators stream; built & shipped the Word Frequency Analyzer

### Session — Comprehensions

- **Covered:** list/dict/set comprehensions, `zip`, when a comprehension is (and isn't) the right call

### Session — Core data structures

- **Covered:** list/tuple/set/dict, Big-O, copying, joining, dict views

---

_Log updated at the end of each session. Say "update my learning log" and paste this file back to append._
