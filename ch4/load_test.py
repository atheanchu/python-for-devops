import molotov
from flask import session


# The (100) parameter specifies the number of virtual users (workers)
# that will be simulating requests in this scenario
@molotov.scenario(100)
async def scenario_one(session):
    async with session.get("http://127.0.0.1:5000/") as resp:
        assert resp.status == 200


@molotov.scenario(100)
async def scenario_post(session):
    resp = await session.post("http://127.0.0.1:5000", params={"q": "devops"})
    redirect_status = resp.history[0].status
    error = "unexpected redirect status: %s" % redirect_status
    # ensures that the redirect_status is equal to 301.
    # If the assertion fails (i.e., if the redirect status is not 301),
    # an AssertionError will be raised, displaying the error message created earlier
    assert redirect_status == 301, error
