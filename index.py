import json
import os

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.lighthouse.v20200324 import lighthouse_client, models



class LighthouseSnapshotManager:
    def __init__(self, secret_id, secret_key, region, instance_id):
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.region = region
        self.instance_id = instance_id

        cred = credential.Credential(secret_id, secret_key)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "lighthouse.tencentcloudapi.com"
        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = lighthouse_client.LighthouseClient(cred, region, clientProfile)
        self.client = client
    
    def describe(self, snapshot_name = None):
        req = models.DescribeSnapshotsRequest()
        params = {
            "Filters": [
                {
                    "Name": "instance-id",
                    "Values": [ self.instance_id ]
                }
            ]
        }
        if snapshot_name:
            params["Filters"].append(
                {
                    "Name": "snapshot-name",
                    "Values": [ snapshot_name ]
                }
            )
        req.from_json_string(json.dumps(params))
        resp = self.client.DescribeSnapshots(req)
        return resp.SnapshotSet

    def create(self, snapshot_name):
        req = models.CreateInstanceSnapshotRequest()
        params = {
            "InstanceId": "lhins-mdickw80",
            "SnapshotName": snapshot_name
        }
        req.from_json_string(json.dumps(params))
        self.client.CreateInstanceSnapshot(req)

    def delete(self, snapshot_name):
        snapshots = self.describe(snapshot_name)
        if len(snapshots) > 0:
            snapshot_id = snapshots[0].SnapshotId
            req = models.DeleteSnapshotsRequest()
            params = {
                "SnapshotIds": [ snapshot_id ]
            }
            req.from_json_string(json.dumps(params))
            self.client.DeleteSnapshots(req)


def main_handler(event, context) -> None:
    secret_id = os.environ.get("SECRET_ID")
    secret_key = os.environ.get("SECRET_KEY")
    region = os.environ.get("REGION")
    instance_id = os.environ.get("INSTANCE_ID")
    snapshot_name = f"SCF-Snapshot-{instance_id}"

    snapshot_manager = LighthouseSnapshotManager(secret_id, secret_key, region, instance_id)
    if len(snapshot_manager.describe(snapshot_name)) > 0:
        print("检测到旧快照存在")
        snapshot_manager.delete(snapshot_name)
        print("删除旧快照成功")
    snapshot_manager.create(snapshot_name)
    print(f"创建新快照成功。快照名称：{snapshot_name}")
