#!/bin/bash
# ...Comment header goes here...
# scripty testing

set -o errexit 

set -o nounset 

set -o pipefail

​main() { 

  for file in *; do

  if [[ -d "${file}" ]]; then

    echo "Directory: ${file}"

  elif [[ -f "${file}" ]]; then

    echo "File: ${file}"

  fi

done

} 

main "${@}"
