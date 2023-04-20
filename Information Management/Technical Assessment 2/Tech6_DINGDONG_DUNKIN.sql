-- making user table
CREATE TABLE "user" (
    id_user NUMERIC(11, 0) NOT NULL,
    name VARCHAR2(50) NOT NULL,
    last_name VARCHAR2(50) NOT NULL,
    email VARCHAR2(50) NOT NULL,
    user_name VARCHAR2(50) NOT NULL,
    password VARCHAR2(50) NOT NULL,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL,
    enabled NUMERIC(1, 0) NOT NULL,
    CONSTRAINT "user_pk" PRIMARY KEY (id_user)
);

--  making task table
CREATE TABLE task (
    id_task NUMERIC(11, 0) NOT NULL,
    name VARCHAR2(50) NOT NULL,
    description VARCHAR2(50) NOT NULL,
    work VARCHAR2(50) NOT NULL,
    id_project VARCHAR2(50) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL,
    enabled NUMERIC(1, 0) NOT NULL,
    CONSTRAINT "task_pk" PRIMARY KEY (id_task)
);

-- making time category
CREATE TABLE time_category (
    id_time_category NUMERIC(11, 0) NOT NULL,
    name VARCHAR2(50) NOT NULL,
    description VARCHAR2(50) NOT NULL,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL,
    enabled NUMERIC(1, 0) NOT NULL,
    CONSTRAINT "time_category_pk" PRIMARY KEY (id_time_category)
);

-- making time sheet
CREATE TABLE time_sheet (
    id_time_sheet NUMERIC(11, 0) NOT NULL,
    name VARCHAR2(50) NOT NULL,
    description VARCHAR2(50) NOT NULL,
    id_project VARCHAR2(50) NOT NULL,
    created_at DATE NOT NULL,
    updated_at DATE NOT NULL,
    enabled NUMERIC(1, 0) NOT NULL,
    id_user NUMERIC(11, 0) NOT NULL,
    CONSTRAINT "time_sheet_pk" PRIMARY KEY (id_time_sheet)
);

-- making time sheet hour
CREATE TABLE time_sheet_hour (
    id_time_sheet_hour NUMERIC(11, 0) NOT NULL,
    id_time_sheet NUMERIC(11, 0) NOT NULL,
    id_user NUMERIC(11, 0) NOT NULL,
    id_time_category NOT NULL,
    id_task NUMERIC(11, 0) NOT NULL,
    quantity NUMERIC(5, 0) NOT NULL,
    description VARCHAR2(50) NOT NULL,
    CONSTRAINT "time_sheet_hour_pk" PRIMARY KEY (id_time_sheet_hour),
    CONSTRAINT "time_sheet_time_sheet_hour_fk" FOREIGN KEY (id_time_sheet) REFERENCES time_sheet,
    CONSTRAINT "user_time_sheet_hour_fk" FOREIGN KEY (id_user) REFERENCES "user",
    CONSTRAINT "time_category_time_sheet_hour_fk" FOREIGN KEY (id_time_category) REFERENCES time_category,
    CONSTRAINT "task_time_sheet_hour_fk" FOREIGN KEY (id_task) REFERENCES task
);
