from sqlalchemy import select, Select
from sqlalchemy.orm import declarative_base, InstrumentedAttribute, class_mapper

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    @classmethod
    def get_select_stmt(
        cls, column_names: list[InstrumentedAttribute] | list[str] | None = None
    ) -> Select:
        """
        Generate a SQLAlchemy SELECT statement for the table with the given column names (take them all if they are not gave).

        ARGS:
            column_names (list[InstrumentedAttribute] | list[str] | None) : a list of column names
                - If None: select all columns (SELECT * FROM table)
                - If list of InstrumentedAttribute: selects the given columns
                - If list of str: selects the columns matching the attribute names
                - else: raise a TypeError
        RETURN:
            sqlalchemy.sql.Select : A SQLAlchemy Select object representing the query.
        """
        if column_names is None:
            return select(cls)

        if all(isinstance(c, str) for c in column_names):
            try:
                selected_columns = [getattr(cls, name) for name in column_names]
            except AttributeError as e:
                mapper = class_mapper(cls)
                valid_names = [col.key for col in mapper.columns]
                raise AttributeError(
                    f"One or more column names are invalid. "
                    f"Valid column names are: {valid_names}"
                ) from e
            return select(*selected_columns)

        if all(isinstance(c, InstrumentedAttribute) for c in column_names):
            return select(*column_names)

        raise TypeError(
            "All items in 'columns' must be of the same type: either all str or all InstrumentedAttribute."
        )