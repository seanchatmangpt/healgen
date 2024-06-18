"""dspy"""
from pathlib import Path

import dspy
import typer
from dspy import Signature, InputField, OutputField

from healgen.utils.dspy_tools import init_dspy

app = typer.Typer()


@app.command(name="new")
def dspy_new():
    """new"""
    typer.echo("Running new subcommand.")


class GenerateHealthSummary(Signature):
    """
    Generate a concise health summary for a patient based on their chart with a specified number of sentences.
    """
    patient_chart = InputField(desc="Detailed patient medical chart.")
    sentence_count = InputField(desc="Exact number of sentences for the summary.")

    health_summary = OutputField(desc="Generated health summary with the specified number of sentences.")


@app.command(name="summary")
def dspy_summary(patient_chart: Path = typer.Argument("fake_chart.txt", help="Detailed patient medical chart"),
                 sentence_count: int = typer.Argument(3, help="Exact number of sentences for the summary")):
    """Use the dspy framework to create a health summary for a patient."""
    print("Generating health summary...")
    init_dspy()
    pred = dspy.Predict(GenerateHealthSummary)
    result = pred.forward(patient_chart=patient_chart.read_text(), sentence_count=str(sentence_count))
    print(result.health_summary)


def main():
    init_dspy()
    sentence_count = 3
    pred = dspy.Predict(GenerateHealthSummary)
    # pred = dspy.ChainOfThought(GenerateHealthSummary)
    result = pred.forward(patient_chart=fake_patient_chart, sentence_count=str(sentence_count))
    print(result.health_summary)


if __name__ == "__main__":
    main()
