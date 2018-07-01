%% Quicksort has O(N lg N) runtime on average.
-module(quicksort).
-export([sort1/1, sort2/1]).

%% Using list's head as the pivot.
%% This can degrades to O(N^2) if the list
%% is originally reverse-sorted.
sort1([]) -> [];
sort1([Pivot|T]) ->
    sort([ X || X <- T, X < Pivot]) ++
	[Pivot] ++
	sort([ X || X <- T, X >= Pivot]).

%% Use Sedgewick's "Median of Three"
%% This circumvents the first issue.
sort2([]) -> [];
sort2([A]) -> [A];
sort2([A,B]) ->
    case A =< B of
	true -> [A,B];
	false -> [B,A]
    end;
sort2(L) ->
    [A,B,C|_] = L,
    [_, M, _] = sort1([A,B,C]),
    Pivot = M,
    sort2([ X || X <- L, X < Pivot]) ++
    [Pivot] ++
    sort2([ X || X <- lists:reverse(L), X > Pivot]).

			  
		      
    
     
    
     

		 
