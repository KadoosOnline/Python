DROP TABLE IF EXISTS teachers;

CREATE TABLE teachers (
    teacher_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_name TEXT NOT NULL,

    -- DEFAULT: the value used when the INSERT does not mention this column.
    department   TEXT DEFAULT 'عمومی'
);
