from click.testing import CliRunner

from iac_jenkins_assistant import main


def test_create_template():
    runner = CliRunner()
    result = runner.invoke(main, ["create-template", "--name", "test"])
    pass


def test_deploy_infra():
    runner = CliRunner()
    result = runner.invoke(
        main, ["deploy-infra", "--template_name", "test", "--number_of_machines", "4"]
    )
    pass


test_create_template()
test_deploy_infra()
