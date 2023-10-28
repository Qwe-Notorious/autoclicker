import flet as ft

def GUIInterface(page: ft.Page):
    # Настройка окна программы
    page.title = "Clickir Control Panel"
    page.window_width = 500
    page.window_height = 550
    page.bgcolor = "#272829"

    textInfo = ft.Text(
        'To start the autoclicker, you need to configure the config. To do this, write how long it takes for the clicker to work (in seconds), how many clicks, and the interval of operation.',
        color=ft.colors.GREEN_400, size=20)

    inputSecends = ft.TextField(label="Seconds", width=200, color=ft.colors.GREEN_400)
    inputMauseButton = ft.TextField(label="Mause left/right", width=200, color=ft.colors.GREEN_400)
    inputClicks = ft.TextField(label="number of clicks", width=200, color=ft.colors.GREEN_400)
    inputInterval = ft.TextField(label="Interval", width=200, color=ft.colors.GREEN_400)

    UIElementsInput = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        inputSecends,
                    ),
                    inputMauseButton,
                    inputClicks,
                    inputInterval,
                ],
            ),
        ],
    )

    bntStart = ft.ElevatedButton(text="Start Clicks", width=200, color=ft.colors.GREEN_400, on_click=m.ClickerMauseButtonn)

    ButtonElement = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    bntStart
                ],
            ),
        ],
    )
    page.add(textInfo, UIElementsInput, ButtonElement)
    # Обновление окна
    page.update()

ft.app(target=GUIInterface)
