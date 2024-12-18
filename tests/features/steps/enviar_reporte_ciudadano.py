from behave import *

use_step_matcher("re")


@step(
    'que un ciudadano ha identificado un problema con tipo "<tipo>", descripción "<descripción>" y ubicación "<ubicación>"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(
        u'STEP: Dado que un ciudadano ha identificado un problema con tipo "<tipo>", descripción "<descripción>" y ubicación "<ubicación>"')