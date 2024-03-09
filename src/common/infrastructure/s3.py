import io


def get_csv_from_bucket(bucket, object_key):
    file = bucket.get(object_key)
    file_content = file['Body'].read().decode()
    stream = io.StringIO(file_content)

    return csv.reader(stream)