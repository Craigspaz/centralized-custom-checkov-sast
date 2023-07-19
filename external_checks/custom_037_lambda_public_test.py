import unittest
import hcl2

from checkov.common.models.enums import CheckResult
from custom_037_lambda_public import check


class TestEC2TerminationProtection(unittest.TestCase):
    def test_failure(self):
        bad_resources = open("./test/custom_037_FAIL_lambda_public.tf", "r")
        hcl_res = hcl2.loads(bad_resources.read())
        bad_resources.close()
        # You can specify individual resources if you want to limit the test scope
        resource_conf = hcl_res["resource"][1]["aws_lambda_function_url"]["test_live"]
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILED, scan_result)

    def test_success(self):
        good_resources = open("./test/custom_037_PASS_lambda_public.tf", "r")
        hcl_res = hcl2.loads(good_resources.read())
        good_resources.close()
        # You can specify individual resources if you want to limit the test scope
        resource_conf = hcl_res["resource"][1]["aws_lambda_function_url"]["test_live"]
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.PASSED, scan_result)


if __name__ == "__main__":
    unittest.main()
