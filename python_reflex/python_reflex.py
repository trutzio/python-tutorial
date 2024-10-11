import reflex as rx

class FormState(rx.State):
    todos: list = []
    def handle_submit(self, form_data: dict):
        self.todos.append(form_data)

def index() -> rx.Component:
    return rx.vstack(
        rx.heading("Neue Aufgabe"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Aufgabe",
                    name="title",
                ),
                rx.input(
                    placeholder="Fälligkeitstermin",
                    name="due_date",
                ),
                rx.hstack(
                    rx.checkbox("Erledigt", name="check")
                ),
                rx.button("Hinzufügen", type="submit"),
                ),
            on_submit=FormState.handle_submit,
            reset_on_submit=True,
        ),
    rx.divider(),
    rx.heading("Alle Aufgaben"),
    rx.text(FormState.todos.to_string()),
    padding="2em",
    )
    

app = rx.App()
app.add_page(index)
