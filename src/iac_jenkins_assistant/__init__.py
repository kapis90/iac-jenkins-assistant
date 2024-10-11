import click
import requests


@click.command()
@click.option("--template_name", required=True, type=str)
@click.option("--number_of_machines", required=True, type=int)
@click.version_option("0.1.0", prog_name="iac_jenkins_assistant")
def main(template_name: str, number_of_machines: int):
    data = {"template_name": template_name, "number_of_machines": number_of_machines}
    response = requests.post("https://httpbin.org/anything", data)
    click.echo(response.request.body)


if __name__ == "__main__":
    main()
