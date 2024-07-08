from cx_Freeze import setup, Executable

setup(
    name="BotWhatsapp",
    version="1.0",
    description="Um bot de mensagens automáticas para whatsapp",
    executables=[Executable("app.py")],
)
