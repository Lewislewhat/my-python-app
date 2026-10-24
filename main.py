import flet as ft

def main(page: ft.Page):
    page.title = "Simple Android App"
    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    counter = 0

    text_display = ft.Text(
        value="Hello from Python!",
        size=28,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.BLUE_600
    )

    counter_label = ft.Text(
        value=f"Clicks: {counter}",
        size=20
    )

    def on_button_click(e):
        nonlocal counter
        counter += 1
        counter_label.value = f"Clicks: {counter}"
        text_display.value = "Button Pressed! 🎉"
        page.update()

    def on_reset_click(e):
        nonlocal counter
        counter = 0
        counter_label.value = f"Clicks: {counter}"
        text_display.value = "Hello from Python!"
        page.update()

    click_button = ft.ElevatedButton(
        text="Click Me!",
        icon=ft.Icons.THUMB_UP,
        on_click=on_button_click
    )

    reset_button = ft.OutlinedButton(
        text="Reset",
        icon=ft.Icons.REFRESH,
        on_click=on_reset_click
    )

    page.add(
        ft.Column(
            [
                text_display,
                counter_label,
                ft.Row(
                    [click_button, reset_button],
                    alignment=ft.MainAxisAlignment.CENTER
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == "__main__":
    ft.run(main)
