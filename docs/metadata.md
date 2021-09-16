
# Metadata & Indexes

## Metadata

In a simple definition, metadata is considered by yardb to be all data relating to the inner workings of the dbms. That is, data relating to your stored data. Such as, for example: data relating to tables that exist in the schema or the columns of a table with their types and sizes in bytes.

Basically the metadata is found in 3 static structure tables: ``information_schema``, ``information_schema_column`` and ``information_schema_catalog``.

The last name is momentarily reserved for structures that will be created in other versions.

---

### `information_schema`

Contains table data divided into two columns: table_name and schema. The schema for now will always be public, later it will allow the creation of more schemas to store the tables.

| column | size (bytes) | type |
| --- | --- | --- |
| table_name | 255 bytes | varchar |
| schema | 255 bytes | varchar |

It can be organized in heap pages as follows:

<table>
    <tr>
        <td>pd_lower (16b) </td>
        <td>pd_upper (16b) </td>
        <td>pointer_1 (16b)</td>
        <td>pointer_2 (16b)</td>
    </tr>
    <tr>
        <td colspan=4 align=center> empty space </td>
    </tr>
    <tr>
        <td colspan=4 align=center> empty space </td>
    </tr>
    <tr>
        <td colspan=2 align=center>
            <table>
                row_2 (255b+255b)
                <tr>
                    <td>table_name_2 (255b)</td>
                    <td>schema_2 (255b)</td>
                </tr>
            </table>
        </td>
        <td colspan=2 align=center>
            <table>
                row_1 (255b+255b)
                <tr>
                    <td>table_name_1 (255b)</td>
                    <td>schema_1 (255b)</td>
                </tr>
            </table>
        </td>
    </tr>
</table>


### `information_schema_column`

Contains data relating to the columns of each table, which can be divided as follows:

| columns | size (bytes) | type |
| --- | --- | --- |
| table_name | 255 | varchar |
| column_name | 255 | varchar |
| nullable | 1 | boolean |
| data_type | 16 | int |
| length | 16 | int |

It can be organized in heap pages as follows:

<table>
    <tr>
        <td>pd_lower (16b) </td>
        <td>pd_upper (16b) </td>
        <td>pointer_1 (16b)</td>
        <td> empty space </td>
    </tr>
    <tr>
        <td colspan=4 align=center> empty space </td>
    </tr>
    <tr>
        <td colspan=4 align=center> empty space </td>
    </tr>
    <tr>
        <td colspan=1 align=center>
            empty space
        </td>
        <td colspan=3 align=center>
            <table>
                row_1 (255b+255b)
                <tr>
                    <td>table_name_1 (255b)</td>
                    <td>column_name_1 (255b)</td>
                    <td>nullable (1b)</td>
                </tr>
                <tr>
                    <td>data_type (16b)</td>
                    <td>length (16b)</td>
                </tr>
            </table>
        </td>
    </tr>
</table>
