import streamlit as st 
import os

# create connection
conn = st.connection(
  name="my_db",
  type="sql",
  dialect="postgresql",
  host=os.getenv("host"),
  port=os.getenv("port"),
  database=os.getenv("database"),
  username=os.getenv("uname"),
  password=os.getenv("password")
)

sql = """
select
  f1.title
  , count(f2.actor_id) as actor_cnt
from film f1
left join film_actor f2 
	on f1.film_id = f2.film_id
group by f1.film_id
;
"""

df = conn.query(sql, ttl="10m")
st.dataframe(df)
