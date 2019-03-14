#!/usr/bin/python
# -*- coding: utf-8 -*-
from core.Console import Console
from threading import Thread

if __name__ == "__main__":
    console = Console()
    Thread(target=console.iniciar_consola).start()