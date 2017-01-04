import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

public class Mancala {
	private int[] board = {4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4, 0};
	private Set<Integer> player0Spots = new HashSet<Integer>();
	private Set<Integer> player1Spots = new HashSet<Integer>();
	private int[] positions = {0, 1, 2, 3, 4, 5};

	public Mancala() {
		int spots = 0;
		while (spots < 6) {
			player0Spots.add(spots);
			spots++;
		}
		spots++;
		while (spots < 13) {
			player1Spots.add(spots);
			spots++;
		}
	}

	public static int[] reverse(int[] arr) {
        int[] copy = new int[arr.length];
        for (int i = arr.length - 1; i >= 0; i--) {
        	copy[arr.length - i - 1] = arr[i];
        }
        return copy;
    }

	public int turn(int player, int position) {
		// assert (player == 0 or player == 1), "Not a valid position"
		// assert (position >= 0 and position <= 5 and type(position) is int), "Not a valid position"
		// calculate starting position
		int curr = player * 7 + position;
		int amount = board[curr];
		// Checking for errors in input
		if (position >= 0 && position <= 5) {
			System.out.println("Invalid Position, must be between 0-5. You will have to pick again");
			return player;
		} else if (amount == 0) {
			System.out.println("You picked an empty space! You will have to pick again.");
			return player;
		}

		board[curr] = 0;
		while (amount > 0) {
			curr = (curr + 1) % board.length;
			if ((curr != 6 && player == 1) || (curr != 13 && player == 0)) {
				board[curr]++;
				amount--;
			}
		}
		if ((player == 0 && curr == 6) || (player == 1 && curr == 13)) {
			return player;
		} else if (board[curr] == 1) {
			boolean correctRange = (player == 0 && player0Spots.contains(curr)) || (player == 1 && player1Spots.contains(curr));
			int opp = 12 - curr;
			if (correctRange && board[opp] != 0) {
				System.out.println("Player " + player + " successfully stole some pieces!");
				int stole = board[opp];
				board[opp] = 0;
				stole += board[curr];
				board[curr] = 0;
				if (player == 0) {
					board[6] += stole;
				} else {
					board[13] += stole;
				}
			}
		}
		return 1 - player;
	}

	public boolean isTerminal(int player) {
		if (player == 0) {
			for (int i = 0; i < 6; i++) {
				if (board[i] != 0) {
					return false;
				}
			}
		} else {
			for (int i = 7; i < 13; i++) {
				if (board[i] != 0) {
					return false;
				}
			}
		}
		System.out.println("Player " + player + " ran out of moves.");
		return true;
	}

	public void cleanUp() {
		int total1 = 0;
		for (int i = 0; i < 6; i++) {
			total1 += board[i];
			board[i] = 0;
		}
		int total2 = 0;
		for (int j = 7; j < 13; j++) { 
			total2 += board[j];
			board[j] = 0;
		}
		board[6] += total1;
		board[13] += total2;
		if (total1 > total2) {
			System.out.println("Player 0 Won! " + board[6] + " to " + board[13] + ".");
		} else if (total1 < total2) {
			System.out.println("Player 1 Won! " + board[13] + " to " + board[6] + ".");
		} else {
			System.out.println("Tie! " + board[13] + " to " + board[6] + ".");
		}
	}


	public void getState() {
		System.out.println();
		System.out.println("---" + Arrays.toString(reverse(positions)) + "---\n");
		System.out.println(Arrays.toString(Arrays.copyOfRange(reverse(board), 0, 7)));
		System.out.println("---" + Arrays.toString(Arrays.copyOfRange(board, 0, 7)));
		System.out.println("\n---" + Arrays.toString(positions) + "---");
		System.out.println();
	}

	public static void main(String[] args) {
		Mancala board = new Mancala();
		Scanner s = new Scanner(System.in);
		int currPlayer = 0;
		while (!board.isTerminal(currPlayer)) {
			board.getState();
			System.out.print("Which position does player " + currPlayer + " want? ");
			int position = s.nextInt();
			currPlayer = board.turn(currPlayer, position);
		}
		board.cleanUp();
		board.getState();
	}
}


