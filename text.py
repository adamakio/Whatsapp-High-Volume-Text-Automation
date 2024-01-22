english_text = {
    "name": "name",
    "number": "number",
    "license_prompt": "Input license key: ",
    "license_success": "User successfully authenticated",
    "license_failed": "Failed to authenticate user.",
    "app_failed": "App failed because of the following error: ",
    "app_restarting": "App restarting in {} seconds",
    "welcome": "Welcome to [bold]SapBro[/bold] Whatsapp Bot",
    "wait_time": {
        "prompt": "Select Internet Speed",
        "info": "[green]INFO:[/green] This adjusts the time between opening the tab and starting the sending.",
        "options": [
            "Slow (20 second wait time)",
            "Medium (15 second wait time)",
            "Fast (10 second wait time)",
            "Very Fast (7 second wait time)",
        ],
        "success": "Internet Speed Set to: {}",
        "error": "Invalid input: {}",
    },
    "import_contacts": {
        "prompt": (
            "Press [green]Enter[/green] to import your contacts list from CSV file\n"
            "Make sure the format of the CSV file matches the one given with the application (contacts.csv)"
        ),
        "success": "You have imported the following contacts successfully:",
        "failure": "Failed to read contacts from filepath: {}",
    },
    "input_messages": {
        "prompt": "Input Messages To Send\n",
        "info": (
            "[green]INFO:[/green]\n"
            "Type in the text or caption as you would like to send it.\n"
            "Use [NAME] where you would like the name of your contact to appear.\n"
            "Use /// to separate paragraphs.\n"
            'Avoid using the following characters: \\, {, }, ".\n'
        ),
        "message": "MESSAGE",
        "text": "TEXT",
        "media": "MEDIA WITH CAPTION (only JPEG is supported currently)",
        "exit": "END OF MESSAGE",
        "prompt_1": "Input text message: ",
        "prompt_2": "Press [green1]Enter[/green1] to select media file",
        "prompt_3": "Input caption: ",
        "error": "INVALID OPTION",
    },
    "delay": {
        "prompt": "Input delay (in seconds) between messages:",
        "info": "[green]INFO:[/green] This adjusts the time between consecutive messages to make the bot seem human.",
        "success": "Successfully set delay to: {} seconds",
        "bounds_error": "Delay must be between {} and {} seconds",
        "error": "Invalid delay input value: {}",
    },
    "confirm_task": {
        "display_messages": "You are sending the following messages:",
        "text_message": "Text Message: {}",
        "media_message": "Media Message: \nMedia Path: {}\nCaption: {}",
        "display_numbers": "To the following numbers:",
        "confirm": "Confirm?",
        "yes": "y",
        "no": "n",
    },
}


spanish_text = {
    "name": "nombre",
    "number": "numero",
    "license_prompt": "Introducir la llave de accesso: ",
    "license_success": "Usuario verificado satisfactoriamente",
    "license_failed": "Fallo al authenticar usuario",
    "app_failed": "Fallo el applicacion por el siguente error: ",
    "app_restarting": "Reiniciando en {} segundos",
    "welcome": "Bienvenido a [bold]SapBro[/bold] Whatsapp Bot",
    "wait_time": {
        "prompt": "Selecciona la velocidad de internet",
        "info": "[green]INFO:[/green] Esto ajusta el tiempo entre abrir la pestaña y comenzar el envío.",
        "options": [
            "Lento (20 segundos de tiempo de espera)",
            "Medio (15 segundos de tiempo de espera)",
            "Rápido (10 segundos de tiempo de espera)",
            "Muy Rápido (7 segundos de tiempo de espera)",
        ],
        "success": "Velocidad de internet seleccionada: {}",
        "error": "Comando introducido inválido: {}",
    },
    "import_contacts": {
        "prompt": (
            "Pulsa [green]Introduce[/green] para importar tu lista de contactos desde un archivo CSV\n"
            "Asegúrese de que el formato del archivo CSV coincida con el proporcionado con la aplicación (contacts.csv)"
        ),
        "success": "La siguiente lista de contactos se importó satisfactoriamente:",
        "failure": "Fallo al leer contactos desde la ubicación: {}",
    },
    "input_messages": {
        "prompt": "Introduzca mensaje para enviar\n",
        "info": (
            "[green]INFO:[/green] \n"
            "Escriba el texto o el pie de foto como le gustaría enviarlo.\n"
            "Utilice [NAME] donde desea que aparezca el nombre de su contacto.n"
            "Utilice /// para separar párrafos.\n"
            'Evitar el uso de los siguientes caracteres: \\, {, }, ".\n'
        ),
        "message": "MENSAJE",
        "text": "TEXTO",
        "media": "MULTIMEDIA CON SUBTITULO (actualmente solo se admite JPEG)",
        "exit": "FIN DEL MENSAJE",
        "prompt_1": "Introduzca mensaje de texto: ",
        "prompt_2": "Presiona [green1]Introducir[/green1] para seleccionar archivo multimedia",
        "prompt_3": "Introduzca subtitulo: ",
        "error": "OPCIÓN INVALIDA",
    },
    "delay": {
        "prompt": "Introduzca tiempo de demora (en segundos) entre mensajes:",
        "info": "[green]INFO:[/green] Esto ajusta el tiempo entre mensajes consecutivos para que el bot parezca humano.",
        "success": "Tiempo de demora satisfactioriamente establecido a: {} segundos",
        "bounds_error": "El tiempo de demora debe ser entre {} y {} segundos",
        "error": "Tiempo de demora inválido, introduzca valor: {}",
    },
    "confirm_task": {
        "display_messages": "Usted está enviando los siguientes mensajes:",
        "text_message": "Mensaje de texto: {}",
        "media_message": "Mensaje Multimedia: \nUbicación Multimedia: {}\nSubtítulo: {}",
        "display_numbers": "A los siguientes número:",
        "confirm": "Confirmar?",
        "yes": "s",
        "no": "n",
    },
}
