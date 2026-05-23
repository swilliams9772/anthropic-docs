# Delete a Message Batch

**Source:** http://platform.claude.com/docs/en/api/deleting-message-batches

Copy page

cURL

# Delete a Message Batch

DELETE/v1/messages/batches/{message\_batch\_id}

Delete a Message Batch.

Message Batches can only be deleted once they've finished processing. If you'd like to delete an in-progress batch, you must first cancel it.

Learn more about the Message Batches API in our [user guide](https://docs.claude.com/en/docs/build-with-claude/batch-processing)

# Path ParametersExpand Collapse

message\_batch\_id: string

ID of the Message Batch.

# ReturnsExpand Collapse

DeletedMessageBatch object { id, type }

id: string

ID of the Message Batch.

type: "message\_batch\_deleted"

Deleted object type.

For Message Batches, this is always `"message_batch_deleted"`.

Delete a Message Batch

cURL

```
curl https://api.anthropic.com/v1/messages/batches/$MESSAGE_BATCH_ID \
    -X DELETE \
    -H 'anthropic-version: 2023-06-01' \
    -H "X-Api-Key: $ANTHROPIC_API_KEY"
```

Response 200

```
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```

# Returns Examples

Response 200

```
{
  "id": "msgbatch_013Zva2CMHLNnXjNJJKqJ2EF",
  "type": "message_batch_deleted"
}
```
