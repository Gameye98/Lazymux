
sqlc(){
# Usage: sqlc db_file sql_script
ex_sqlc=$(cat <<DOCUMENT
create table test (id integer primary key, name text, age number);
insert into test (name, age) values('dtlily', 16);
select * from test;
DOCUMENT
)
if test -z "$1"; then
	if test ! -e test.db; then
		user_db="test.db"
	else
		for i in $(seq 0 20); do
			if test ! -e "test${i}.db"; then
				user_db="test${i}.db"
				break
			fi
		done
	fi
else
	user_db="$1"
fi
if test -z "$2"; then
	printf "$ex_sqlc" > $PREFIX/tmp/sqlc_test.sql
	sql_script="$PREFIX/tmp/sqlc_test.sql"
else
	sql_script="$2"
fi
echo -e "\x1b[92msql query processor 1.0\x1b[0m"
echo -e "\x1b[92mdatabase: \x1b[93m${user_db}\x1b[0m"
echo -e "\x1b[92msql script: \x1b[93m${sql_script}\x1b[92m; $(cat ${sql_script} | wc -c)B\x1b[0m"
total_lines=$(cat ${sql_script} | wc -l)
for((x = 0;x <= ${total_lines};x++)); do
	sql_query=$(python -c "print(open('${sql_script}','r').read().split('\n')[${x}].strip())")
	echo -e "\x1b[92m-- query: \x1b[93m${sql_query}\x1b[0m"
	return_output=$(sqlite3 ${user_db} "${sql_query}")
	if test "$(echo ${return_output} | grep Error)"; then
		echo -e "\x1b[91m${return_output}\x1b[0m"
	fi
	if [[ "${return_output}" != "" ]]; then
		echo -e "\x1b[92m-- output:\x1b[0m"
		echo -e "\x1b[93m${return_output}\x1b[0m"
	fi
done
}
