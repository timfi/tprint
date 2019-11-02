from typing import List, Optional, Dict, Sequence, Union


__all__ = ("tformat", "tprint")


def tformat(
    data: Union[Dict[str, Sequence], Sequence],
    *,
    as_columns: bool = False,
    headers: Optional[Sequence[str]] = None,
    alignments: Optional[str] = None,
    formattings: Optional[str] = None,
) -> str:
    """
    Format a dictionary or list as a table.
    
    :param data: table data
    :param as_columns: interpret given data as collection of columns
                       instead of as rows
    :param headers: sequence of column headers
                    (Defaults to enumerating the columns if headers
                     can't be extracted from data)
    :param alignments: string with alignments per column
                       (Defaults to left alignment for all columns
                        or those skipped with spaces)
    :param formattings: string with formattings per column
                        (Defaults to string casting for all columns
                         or those skipped with spaces)
    """

    if isinstance(data, list):
        data_ = data if as_columns else zip(*data)  # transpose data if given as rows
        if headers is not None:
            data_ = dict(zip(headers, data_))
        else:
            data_ = dict(enumerate(data_))
    elif isinstance(data, dict):
        if as_columns:
            if headers is not None:
                data_ = dict(zip(headers, data.values()))
            else:
                data_ = data
        else:
            data_ = [tuple(data.keys()), *data.values()]
            if headers is not None:
                data_ = dict(zip(headers, data_))
            else:
                data_ = dict(enumerate(data_))
    else:
        raise TypeError(f"Can't make a table out of: {type(data)}.")

    alignments = alignments or "<" * len(data_)
    formattings = formattings or " " * len(data_)

    columns: List[List[str]] = list()
    for header, alignment, formatting, column in zip(
        data_.keys(), alignments, formattings, data_.values()
    ):
        raw_format = f"{{val:{formatting}}}" if formatting != " " else "{val!s}"
        width = max(
            len(str(header)), *(len(raw_format.format(val=cell)) for cell in column)
        )
        alignment = alignment if alignment != " " else ""
        header_format_str = f"{{val:<{width}}}"
        cell_format_str = (
            f"{{val:{alignment}{width}{formatting}}}"
            if formatting != " "
            else f"{{val!s:{alignment}{width}}}"
        )
        columns.append(
            [
                header_format_str.format(val=header),
                "-" * width,
                *[cell_format_str.format(val=cell) for cell in column],
            ]
        )
    return "\n".join(
        " | ".join(cell) if i != 1 else "-+-".join(cell)
        for i, cell in enumerate(zip(*columns))
    )


def tprint(
    data: Union[Dict[str, Sequence], Sequence],
    *,
    as_columns: bool = False,
    headers: Optional[Sequence[str]] = None,
    alignments: Optional[str] = None,
    formattings: Optional[str] = None,
) -> None:
    """
    Print a dictionary or list as a table.
    
    :param data: table data
    :param as_columns: interpret given data as collection of columns
                       instead of as rows
    :param headers: sequence of column headers
                    (Defaults to enumerating the columns if headers
                     can't be extracted from data)
    :param alignments: string with alignments per column
                       (Defaults to left alignment for all columns
                        or those skipped with spaces)
    :param formattings: string with formattings per column
                        (Defaults to string casting for all columns
                         or those skipped with spaces)
    """

    print(
        tformat(
            data,
            as_columns=as_columns,
            headers=headers,
            alignments=alignments,
            formattings=formattings,
        )
    )
