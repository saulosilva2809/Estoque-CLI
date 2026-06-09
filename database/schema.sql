CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    description TEXT,
    price REAL NOR NULL,
    quantity INTEGER NOT NULL,
    stock_min INTEGER,

    category_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,

    created_at TEXT NOT NULL,

    FOREIGN KEY (category_id)
        REFERENCES categories(id),

    FOREIGN KEY (supplier_id)
        REFERENCES suppliers(id)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    description TEXT,

    created_at TEXT NOT NULL
);

CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    city TEXT,

    created_at TEXT NOT NULL
);

CREATE TABLE stock_movements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    product_id INTEGER NOT NULL,

    movement_type TEXT NOT NULL,
    quantity INTEGER NOT NULL,

    created_at TEXT NOT NULL,

    FOREIGN KEY (product_id)
        REFERENCES product(id)
);