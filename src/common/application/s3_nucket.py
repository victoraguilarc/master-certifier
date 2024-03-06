

class S3Bucket(object):
    def __init__(self, bucket_url):
        self._bucket_url = bucket_url
        self._resource = boto3.resource('s3')

    def get(self, file_name):
        return self._resource.Object(self._bucket_url, file_name).get()

    def upload(self, file_name, file_content, content_type: Optional[str] = None):
        optional_params = {'ContentType': content_type}
        return self._resource.Object(self._bucket_url, file_name).put(
            Body=file_content,
            **remove_none_values(optional_params),
        )

    def delete(self, file_name):
        return self._resource.Object(self._bucket_url, file_name).delete()

    def get_url(self, file_name):
        return 'https://{bucket_url}.s3.amazonaws.com/{file_name}'.format(
            bucket_url=self._bucket_url,
            file_name=file_name,
        )

    def read(self, file_name):
        return self.get(file_name)['Body'].read()