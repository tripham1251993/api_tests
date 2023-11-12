from pytest_bdd import scenarios
from tests.api.steps_def.auth_steps import *

scenarios(
	"features/auth.feature",
)
