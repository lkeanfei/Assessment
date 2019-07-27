import pytest

import os
from junit_xml import TestCase, TestSuite
from pytest import  hookspec
from lib.MobileDriver import MobileDriver
# global testCaseList
# testCaseList = []\

testCaseDictList = {}
testScriptList = []
testSuiteList = []
import logging

topPath = os.path.dirname(__file__)

if os.path.exists(topPath+'/test.log'):
    os.remove(topPath + '/test.log')
logging.basicConfig(format='%(asctime)s - %(message)s' , filename = topPath+'/test.log',level=logging.INFO)


@pytest.fixture(scope="session", autouse=True)
def callattr_ahead_of_alltests(request):
    a = request
    # print ("callattr_ahead_of_alltests called")
    yield "123"
    a = request
    # print('finished everything')

    with open(topPath + '/output.xml' , 'w') as f:
        TestSuite.to_file(f, testSuiteList, prettyprint=True)

# def pytest_sessionfinish(session, exitstatus):
#
#     s = session
#     tests = s._node_cache
#     print('finished!')
def generateTestStepsSummary(stepsList):

    stepsSummary = "\r\n"
    for step in stepsList:
        status = "....passed"
        if step["failed"]:
            status = "....failed"

        stepsSummary = stepsSummary + step["keyword"] + " " + step["name"] + status + "\r\n"

    return stepsSummary


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):

    # print('runtest makerepot')
    outcome = yield
    rep = outcome.get_result()
    testScript = rep.fspath
    scriptName = os.path.basename(testScript)


    testname = ""
    try:
        testname = rep.item['name']
    except:
        testname = rep.nodeid

    if rep.when == 'call':
        scenario = rep.scenario
        steps = scenario["steps"]
        durInSeconds = rep.duration
        # for step in steps:
        #     print("********" + step["name"] + ": " + str(step["failed"]))

        stepsSummary = generateTestStepsSummary(steps)
        # print("********name " + testname + " : " + rep.outcome )
        # logging.getLogger().info('new Test CAse ' + testname)
        testCase = TestCase(testname, '', durInSeconds, stepsSummary)
        # logging.getLogger().info('Testname is ' + testname)

        if rep.failed:
            testCase.add_failure_info(rep.longreprtext)

        testCaseDictList[item.fspath.strpath].append(testCase)
        # logging.getLogger().info('Teswqwqwt case list is ' + str(len(testCaseList)))
        # print('len ' + str(len(testCaseList)) + '.Appending testcaselist ' + testCase.name)


def pytest_runtest_protocol(item, nextitem):

    logging.getLogger().info('Runtest protocol for ' + item.fspath.strpath  + ". script list " + ",".join(testScriptList) )

    if item.fspath.strpath not in testScriptList:
        testScriptList.append(item.fspath.strpath)
        # testCaseList.clear()
        testCaseDictList[item.fspath.strpath] = []
        logging.getLogger().info("Cleared tesCaseList! it is a new script! " + item.fspath.strpath)

def pytest_addoption(parser):
    parser.addoption("--os", action="store", default="",
        help="The mobile OS")


@pytest.fixture
def mobileDriver(request):

    mobileOS = request.config.getoption("--os")

    mobiledriver = MobileDriver(mobileOS)


    return mobiledriver



def pytest_runtest_teardown(item):
    # called for running each test in 'a' directory
    localPath = item.fspath
    baseScript = os.path.basename(item.fspath.strpath)

    tsObj = next((x for x in testSuiteList if x.name == baseScript), None)

    # print("runtest teardown for " + baseScript + " : " + str(len(testCaseList)))


    if tsObj == None:
        # logging.getLogger().info(' Tear down Test suite ' + baseScript + ' with test cases ' + str(len(testCaseList)))
        ts = TestSuite( baseScript, testCaseDictList[item.fspath.strpath])
        testSuiteList.append(ts)


