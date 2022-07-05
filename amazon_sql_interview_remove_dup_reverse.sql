# remove reverse rows

select *
from table t
where t.rowid not in
(select t2.rowid
from table t1, table t2
where t1.a = t2.b and t1.b = t2.a and t1.a > t2.a
)