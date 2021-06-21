#!/bin/bash
# ...Comment header goes here...
# scripty testing

set -o errexit
set -o nounset
set -o pipefail

main() {
  arg1="${1}"
  arg2="${2}"
  files=0
  specific_files=0
  directories=0
  for file in ${arg1}; do
#    echo "File: ${file}"
    if [[ -d "${file}" ]]; then
      (( directories += 1 ))
    elif [[ -f "${file}" ]]; then
      (( files += 1 ))
        if [[ "${file}" =~ $arg2 ]]; then
          (( specific_files += 1 ))
        fi
    fi
  done

  echo "Files: ${files}"
  echo "${arg2} files: ${specific_files}"
  echo "Directories: ${directories}"
}
main "${@}"
