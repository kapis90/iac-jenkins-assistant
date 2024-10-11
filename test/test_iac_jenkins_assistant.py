from click.testing import CliRunner

from iac_jenkins_assistant import main

runner = CliRunner()
result = runner.invoke(main, ["--template_name", "test"])
