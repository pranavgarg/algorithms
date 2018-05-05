-module(mergesort).
-author("Panisuan Joe Chasinga <jo.chasinga@gmail.com").
-export([mergesort/1, half/1, half/3, merge/3]).

half([]) -> {[], []};
half([X]) -> {[X], []};
half([X,Y]) -> {[X], [Y]};
half(L) -> 
    Len = length(L),
    half(L, {0, Len}, {[], []}).

half([], _, {Acc1, Acc2}) ->
    {lists:reverse(Acc1), lists:reverse(Acc2)};
half([X], _, {Acc1, Acc2}) -> 
    {lists:reverse(Acc1), lists:reverse([X | Acc2])};
half([H|T], {Cnt, Len}, {Acc1, Acc2}) -> 
    case Cnt >= (Len div 2) of
	true -> half(T, {Cnt + 1, Len}, {Acc1, [H|Acc2]});
	false -> half(T, {Cnt + 1, Len}, {[H|Acc1], Acc2})
    end.

mergesort([]) -> [];
mergesort([A]) -> [A];
mergesort([A, B]) ->
    case A =< B of
	true -> [A,B];
	false -> [B,A]
    end;
mergesort(L) ->
    {Left, Right} = half(L),
    Left_ = mergesort(Left),
    Right_ = mergesort(Right),
    merge(Left_, Right_, []).

merge([], [], Acc) -> Acc;
merge([], [H|T], Acc) -> [H | merge([], T, Acc)];
merge([H|T], [], Acc) -> [H | merge(T, [], Acc)];
merge([Ha|Ta], [Hb|Tb], Acc) ->
    case Ha =< Hb of
	true -> [Ha|merge(Ta, [Hb|Tb], Acc)];
	false -> [Hb|merge([Ha|Ta], Tb, Acc)]
    end.


    

