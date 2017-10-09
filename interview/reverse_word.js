// Basic string recursive reversal for better 
// understanding of recursive function.
'use strict';

function reverse(word) {
  if (word === "") 
    return word;

  var subProblem = word.slice(1, word.length);
  console.log(`subProblem: ${subProblem}`);

  var subSolution = reverse(subProblem);
  console.log(`subSolution: ${subSolution}`);

  var solution = subSolution + word[0];

  return solution;
}

// Test it out...
console.log(reverse("redrum"));

