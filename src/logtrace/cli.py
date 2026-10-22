#!/usr/bin/env python3
import click,re
from collections import Counter
from rich.console import Console
console=Console()
@click.group()
def main(): pass
@main.command()
@click.option('--file',required=True)
def analyze(file):
    with open(file) as f:
        lines=f.readlines()
    errors=sum(1 for l in lines if 'ERROR' in l)
    warns=sum(1 for l in lines if 'WARN' in l)
    console.print(f'Errors: {errors}, Warnings: {warns}')
if __name__=='__main__': main()
