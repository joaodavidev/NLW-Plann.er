from sqlite3 import Connection

class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_links(self, links_infos: dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            '''
                INSERT INTO link
                    (id, trip_id, link, title)
                VALUES
                (?, ?, ?, ?)
            ''',    (
                links_infos["id"],
                links_infos["trip_id"],
                links_infos["link"],
                links_infos["title"],
            )
        )
        self.__conn.commit()