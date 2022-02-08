from datetime import date


class Menu:
    def __init__(self):
        self._notebook = Notebook()

    def show_note(self, note_id):
        note_obj = self._notebook.search(str(note_id))
        if note_obj != None:
            print("="*20)
            print(f"id: {note_obj.id}")
            print(f"memo: {note_obj.memo}")
            print(f"tags: {', '.join(note_obj.tags)}")
            print("="*20)
        else:
            print("not found")

    def search_note(self, key_filter):
        note_obj = self._notebook.search(key_filter)
        print(f"note id = {note_obj.id}")

    def add_note(self, memo, tags):
        self._notebook.new_note(memo, tags)
        return self

    def modify_note(self, note_id, memo):
        self._notebook.modify_memo(note_id, memo)

    def modify_tag(self, note_id, tags):
        self._notebook.modify_tags(note_id, tags)


class Notebook:
    def __init__(self):
        self._notes = []

    def search(self, key_filter):
        if isinstance(key_filter, str):
            for note in self._notes:
                if note.match(key_filter):
                    return note
        else:
            print('string only')

    def new_note(self, memo, tags):
        if isinstance(memo, str) and isinstance(tags, list):
            self._notes.append(Note(memo, date.today, tags))
        else:
            print("memo is string and tags is list")

    def modify_memo(self, note_id, memo):
        for note in self._notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        for note in self._notes:
            if note.id == note_id:
                note.tags = tags
                break

    @property
    def notes(self):
        return self._notes


class Note:
    no_id = 0

    def __init__(self, memo, creation_date, tags):
        Note.no_id += 1
        self._id = Note.no_id
        self._memo = memo
        self._creation_date = creation_date
        self._tags = tags

    @property
    def id(self):
        return self._id

    @property
    def memo(self):
        return self._memo

    @property
    def creation_date(self):
        return self._creation_date

    @property
    def tags(self):
        return self._tags

    @memo.setter
    def memo(self, new_memo):
        if isinstance(new_memo, str):
            self._memo = new_memo
        else:
            print("string only")

    @tags.setter
    def tags(self, new_tags):
        if isinstance(new_tags, list):
            self._tags = new_tags
        else:
            print("list only")

    def match(self, search_filter):
        if isinstance(search_filter, str):
            if search_filter in self._memo:
                return True
            for tag in self._tags:
                if tag == search_filter:
                    return True
            if search_filter == str(self._id):
                return True
            return False
        else:
            print("str only")


menu01 = Menu()

menu01.add_note("hello world", ["python", "oop"]).add_note(
    "goodbye", ["programming"]).add_note("hello 3", ["python", "oop"])
menu01.search_note("hello")
menu01.show_note(1)
menu01.modify_note(1, "hello from kmitl")
menu01.modify_tag(1, ["oop", "UML"])
menu01.show_note(1)
menu01.search_note("programming")
menu01.show_note(2)

