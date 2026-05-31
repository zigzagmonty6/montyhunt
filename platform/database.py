"""
Latin GCSE Mastery Platform — Database helpers
"""
import sqlite3
import contextlib
import os

# Absolute path so the DB is always found regardless of working directory
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "latin_gcse.db")

def init_db():
    with get_db() as db:
        db.executescript("""
            CREATE TABLE IF NOT EXISTS pupils (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL UNIQUE,
                year_group TEXT NOT NULL DEFAULT '10'
            );

            CREATE TABLE IF NOT EXISTS pupil_progress (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pupil_id INTEGER NOT NULL,
                set_id INTEGER NOT NULL,
                status TEXT NOT NULL DEFAULT 'locked',
                best_score REAL NOT NULL DEFAULT 0,
                time_seconds INTEGER DEFAULT 0,
                completed_at TEXT DEFAULT NULL,
                UNIQUE(pupil_id, set_id),
                FOREIGN KEY(pupil_id) REFERENCES pupils(id)
            );

            CREATE TABLE IF NOT EXISTS attempt_log (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pupil_id INTEGER NOT NULL,
                set_id INTEGER NOT NULL,
                question_type TEXT,
                question_text TEXT,
                pupil_answer TEXT,
                correct_answer TEXT,
                result TEXT,
                time_taken_ms INTEGER DEFAULT 0,
                created_at TEXT DEFAULT (datetime('now')),
                FOREIGN KEY(pupil_id) REFERENCES pupils(id)
            );

            CREATE TABLE IF NOT EXISTS settings (
                key TEXT PRIMARY KEY,
                value TEXT
            );

            CREATE TABLE IF NOT EXISTS feedback_msgs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                pupil_id INTEGER,
                pupil_name TEXT,
                set_id INTEGER,
                set_title TEXT,
                note TEXT NOT NULL,
                read_by_teacher INTEGER NOT NULL DEFAULT 0,
                created_at TEXT DEFAULT (datetime('now'))
            );
        """)
        # Seed pupils from STUDENTS_Y10 list
        from data import STUDENTS_Y10
        for name in STUDENTS_Y10:
            db.execute(
                "INSERT OR IGNORE INTO pupils (first_name, year_group) VALUES (?, '10')", (name,)
            )
        # Unlock all introduction sets (node 0) and node 5 first set for all pupils
        from data import SETS
        # Node 0 (reference) always available; for Node 5, only unlock the first set
        node5_sets = sorted([s for s in SETS if s["node"] == 5], key=lambda x: x["id"])
        node5_first_id = node5_sets[0]["id"] if node5_sets else None
        always_available_ids = [s["id"] for s in SETS if s["node"] == 0]
        if node5_first_id:
            always_available_ids.append(node5_first_id)
        pupils = db.execute("SELECT id FROM pupils").fetchall()
        for p in pupils:
            for sid in always_available_ids:
                db.execute(
                    """INSERT INTO pupil_progress (pupil_id, set_id, status, best_score)
                       VALUES (?, ?, 'available', 0)
                       ON CONFLICT(pupil_id, set_id) DO UPDATE SET
                       status = CASE WHEN status = 'locked' THEN 'available' ELSE status END""",
                    (p["id"], sid)
                )

@contextlib.contextmanager
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()
