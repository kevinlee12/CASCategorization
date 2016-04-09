#!/bin/sh

starting_dir=$(pwd)
license_num_lines=$(wc -l < scripts/license_header)
license_header=$(cat scripts/license_header)

for f in $(find . -name '*.py' | grep -vE '__|migrations');
do
	top_of_file=$(head -n ${license_num_lines} $f)
	if [[ "${top_of_file}" != "${license_header}" ]]; then
		echo "Applying license header to ${f}"
		cat "scripts/license_header" <(echo) "${f}" > "${f}.new"
		mv "${f}.new" "${f}"
	fi
done

exit
