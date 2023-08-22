/* FINAL UPDATE LOG:
	- Seth: 04/21/23 @ 8:14pm
	- Karis: 04/21/23 @ 09:25pm
	- Abdallah: 04/22/23 @ 2:20am
	- Karis: 04/22/23 @ 4:50pm
	- Riley: 04/22/23 @ 5:25pm
	- Logan: 04/22/23 @ 5:45pm
	- Karis: 04/22/23 @ 6:13pm
	- Seth: 04/22/23 @ 6:50pm
	- Karis: 04/22/23 @ 11:45pm
	- Seth: 04/25/23 @ 12:30pm
	- Collin: 04/25/23 @ 12:55pm
*/

#include <iostream>
#include <cmath>
#include <string>
#include <cstdlib>
#include <ctime>


using namespace std;


void stapler_counter(double*, double*, double*, double*, double*); // Karis Land
void stapler_upgrader(double*, double*, double*); // Karis Land
void coworker_upgrader(double*, double*, double*); // Logan Tetrick
void boss_upgrader(double& staple_count, double& cUpgrade2, double& B_upgrade_cost); // Abdallah Mohamed
void new_branch_multiplier(double*, double*, double*, double*, double*); // Riley Grace


int main() {

	// GAME doubleRO VARIABLES
	string player_Name;
	char choice_Y_N;
	string business_goal;
	string business_name;

	// SHOP VARIABLES
	double shop = 0;
	double s = 0, c = 0, b = 0, n = 0; //Seth - used to notify of new upgrade once

	// MAIN GAME VARIABLES
	char enter = '\0'; // stores the enter character - '\n'
	double staple_count = -1; // stores the staple count // used in all upgrades deducted by cost
	double* ptr_staple_count = &staple_count; // use with upgrade functions to subtract cost from staple count

	// STAPLER UPGRADE VARIABLES:
	double sUpgrade1 = 0; // stores staple upgrade level
	double* ptr_sUpgrade1 = &sUpgrade1;
	double S_upgrade_cost = 100; // stores staple upgrade cost level 
	double* ptr_S_upgrade_cost = &S_upgrade_cost;
	double initalS_upgrade_cost = S_upgrade_cost;

	// COWORKER UPGRADE VARIABLES: 
	double cUpgrade2 = 1; // stores coworker upgrade //Sets the value the coworker will add initally 
	double* ptr_cUpgrade2 = &cUpgrade2;
	double C_upgrade_cost = 500; // stores cost of coworker upgrade
	double* ptr_C_upgrade_cost = &C_upgrade_cost;


	// BOSS UPGRADE VARIABLES:
	double bUpgrade3 = 0;
	double* ptr_bUpgrade3 = &bUpgrade3;
	double B_upgrade_cost = 1000;
	double* ptr_B_upgrade_cost = &B_upgrade_cost;

	// NEW BRANCH UPGRADE VARIABLES: 
	double NB_Upgrade4 = 0;
	double* ptr_NB_Upgrade4 = &NB_Upgrade4;
	double NB_upgrade_cost = 3000;
	double* ptr_NB_upgrade_cost = &NB_upgrade_cost;


	cout << "******************_______STAPLE MASHER GAME______***********************" << endl << endl;
	cout << "****************_______STAPLE MASHER GAME______*********************" << endl << endl;
	cout << "***********_______STAPLE MASHER GAME______*********************" << endl << endl;
	cout << endl;
	cout << "       Welcome to the office!" << endl << endl;
	cout << "  Having a case of the Mondays are we?" << endl << endl;
	cout << "  Well you've come to the right place!" << endl << endl;
	cout << endl;
	cout << "  Let's start by getting to know each other." << endl;
	cout << "  Please enter your name : ";
	cin >> player_Name;
	system("cls");
	cout << endl << endl << endl << endl << endl << endl << endl;
	cout << "  Great! It's nice to meet you, " << player_Name << "!" << endl;
	cout << endl;
	cout << "  My name is Clip and I'm here to help you build a giant pile of staples." << endl;
	cout << endl;
	cout << endl;
	cout << "  Are you ready to mash?!" << endl;
	cout << "  Type Y or N: ";
	cin >> choice_Y_N;
	while ((choice_Y_N == 'N') || (choice_Y_N == 'n')) {
		cout << endl;
		cout << "  See you at the water cooler, quitter!!!";
		cout << endl << endl;
		return 1;
	}
	system("cls");
	cout << endl << endl;
	cout << "  HOW TO PLAY:" << endl;
	cout << endl;
	cout << "  1. Each time you press the enter key a stapler is mashed and generates one staple." << endl;
	cout << endl;
	cout << "    2. Each staple is added to your resources." << endl;
	cout << endl;
	cout << "      3. Staples can be used to purchase stapler upgrades." << endl;
	cout << endl;
	cout << "  Eventually you will become the CEO of New Branches and broaden your business!" << endl << endl;
	cout << "  *** What type of business would you like to grow: ";
	cin.ignore();
	getline(cin, business_goal);
	cout << "  *** And what would you like to name your business: ";
	getline(cin, business_name);
	system("cls");
	cout << endl << endl << endl << endl << endl << endl << endl;
	cout << "  " << business_name << " is a great name for a business in " << business_goal << "!" << endl << endl;
	cout << "  Alrighty then! Let's get you mashing " << player_Name << " to see if you can't work your way" << endl << "  to the top of the " << business_goal << " business! (Hit Enter) " << endl << endl;
	cout << endl << endl << endl; // Karis Land

	while (true) {
		enter = cin.get();
		if (enter == 's' || enter == 'S') { // Seth Gibbs	
			system("cls");
			cout << endl << endl << endl << endl << endl;
			cout << endl << " ***** WELCOME TO THE UPGRADE SHOP! ***** " << endl << endl;
			cout << "You currently have [ " << staple_count << " ] STAPLES for purchasing upgrades!" << endl << endl;
			cout << "| | | You currently have [ " << staple_count << " ] STAPLES for purchasing upgrades!" << endl << endl;
			cout << "| | | STAPLER EFFICIENCY: " << sUpgrade1 + 1 << endl;
			cout << "| | | COWORKER EFFICIENCY: " << cUpgrade2 << endl;
			cout << "| | | BOSSES BOSSINESS: " << cUpgrade2 + bUpgrade3 << endl;
			cout << "| | | NEW BRANCHES ATTAINED: " << NB_Upgrade4 << endl << endl;
			cout << " \tAVAILABLE UPGRADES:" << endl;
			cout << " \t[PRESS 2] Staple Multiplier Upgrade: COSTS " << S_upgrade_cost << " STAPLES" << endl;
			cout << " \t[PRESS 3] Extra Coworkers Upgrade: COSTS " << C_upgrade_cost << " STAPLES" << endl; //Doesn't work yet but adding anyways - R
			cout << " \t[PRESS 4] Boss Upgrade: COSTS " << B_upgrade_cost << " STAPLES" << endl;
			cout << " \t[PRESS 5] New Branch Upgrade: COSTS " << NB_upgrade_cost << " STAPLES" << endl;
			// Seed the random number generator // Collin Crook
			srand(time(0));

			// Define an array of office jokes
			string jokes[] = {
				"\n\nWhy did the computer go to the doctor? Because it had a virus!",
				"\n\nWhy did the coffee file a police report? Because it got mugged!",
				"\n\nWhat does the baby computer call his father? Data!",
				"\n\nWhy do I drink coffee? I like to do stupid things faster and with more energy"
			};

			// Generate a random index to select a joke from the array
			int index = rand() % 4;

			// Print the selected joke
			cout << jokes[index] << endl;


			cin >> shop;// opens the shop (will have to add upgrades added later) - Seth
		} 

		if (enter == '\n') {
			stapler_counter(ptr_staple_count, ptr_sUpgrade1, ptr_cUpgrade2, ptr_bUpgrade3, ptr_NB_Upgrade4);
			cout << "Staple count: " << "[ " << staple_count << " ]                      [PRESS S] TO ENTER UPGRADE SHOP" << endl;
		}
		if (staple_count == S_upgrade_cost && s == 0) {
			cout << endl << endl << endl;
			cout << player_Name << "! You now have enough staples to purchase a STAPLER Upgrade!" << endl << endl;
			cout << "[PRESS 1] to enter UPGRADE SHOP. " << endl;
			cout << "[PRESS 0] to continue mashing!";
			cin >> shop;
		}
		else if (staple_count == C_upgrade_cost && c == 0) {
			cout << endl << endl << endl;
			cout << player_Name << "! You now have enough staples to purchase a COWORKER Upgrade!" << endl << endl;
			cout << "[PRESS 1] to enter UPGRADE SHOP. " << endl;
			cout << "[PRESS 0] to continue mashing!";
			cin >> shop;
		}
		else if (staple_count == B_upgrade_cost && b == 0) {
			cout << endl << endl << endl;
			cout << player_Name << "! You now have enough staples to purchase a BOSS Upgrade!" << endl << endl;
			cout << "[PRESS 1] to enter UPGRADE SHOP. " << endl;
			cout << "[PRESS 0] to continue mashing!";
			cin >> shop;
		}
		else if (staple_count == NB_upgrade_cost + 3 && n == 0) { // due to incremental increase doesn't hit exactly on 3000.
			cout << endl << endl << endl;
			cout << player_Name << "! You now have enough staples to purchase a NEW BRANCH Upgrade!" << endl << endl;
			cout << "[PRESS 1] to enter UPGRADE SHOP. " << endl;
			cout << "[PRESS 0] to continue mashing!";
			cin >> shop;
		} //Seth - these detect if you bought an upgrade and will tell you once you reach one only once

		if (shop == 1) {
			system("cls");
			cout << endl << endl << endl << endl << endl;
			cout << endl << " ***** WELCOME TO THE UPGRADE SHOP! ***** " << endl << endl;
			cout << "| | | You currently have [ " << staple_count << " ] STAPLES for purchasing upgrades!" << endl << endl;
			cout << "| | | STAPLER EFFICIENCY: " << sUpgrade1 + 1 << endl;
			cout << "| | | COWORKER EFFICIENCY: " << cUpgrade2 << endl;
			cout << "| | | BOSS BOSSINESS: " << cUpgrade2 + bUpgrade3 << endl;
			cout << "| | | NEW BRANCHES ATTAINED: " << NB_Upgrade4 << endl << endl;
			cout << " \tAVAILABLE UPGRADES:" << endl;
			cout << " \t[PRESS 2] Staple Multiplier Upgrade: COSTS " << S_upgrade_cost << " STAPLES" << endl;
			cout << " \t[PRESS 3] Extra Coworkers Upgrade: COSTS " << C_upgrade_cost << " STAPLES" << endl; //Doesn't work yet but adding anyways - R
			cout << " \t[PRESS 4] Boss Upgrade: COSTS " << B_upgrade_cost << " STAPLES" << endl;
			cout << " \t[PRESS 5] New Branch Upgrade: COSTS " << NB_upgrade_cost << " STAPLES" << endl;
			cin >> shop;
		}
		// STAPLER UPGRADE PURCHASE:
		if (shop == 2) {
			if (staple_count >= S_upgrade_cost) {
				stapler_upgrader(ptr_sUpgrade1, ptr_S_upgrade_cost, ptr_staple_count);
				system("cls");
				cout << endl << endl << endl << endl << endl;
				cout << endl << "Upgrade Purchased!" << endl << endl;
				cout << "\tYour stapler is now more powerful! And will mash " << sUpgrade1 + 1 << " staples at a time!" << endl;
				cout << endl << endl << "[Press 1] to return to UPGRADE SHOP." << endl;
				cout << "[Press 0] to continue mashing!" << endl;
				cin >> shop;
				s = 1;
			}
			else {
				cout << "You can't afford this!" << endl << endl << endl;
				cout << "Press 0 to leave the shop" << endl;
				cin >> shop;
				system("cls");
				cout << endl << endl << endl << endl << endl;
				// If someone presses a letter on keyboard here the program breaks
			}
		}
		// COWORKER UPGRADE PURCHASE: 
		else if (shop == 3) {
			if (staple_count >= C_upgrade_cost) {
				coworker_upgrader(ptr_cUpgrade2, ptr_C_upgrade_cost, ptr_staple_count);
				system("cls");
				cout << endl << endl << endl << endl << endl;
				cout << endl << "Upgrade Purchased!" << endl << endl;
				cout << "\tYou now have " << *ptr_cUpgrade2 << " coworkers mashing staplers along with you!" << endl;
				cout << endl << endl << "[Press 1] to return to UPGRADE SHOP." << endl;
				cout << "[Press 0] to continue mashing!" << endl;
				cin >> shop;
				c = 1;
			}
			else {
				cout << "You can't afford this!" << endl << endl << endl;
				cout << "Press 0 to leave the shop" << endl;
				cin >> shop;
				system("cls");
				cout << endl << endl << endl << endl << endl;
			}
		}

		// BOSS UPGRADE PURCHASE: 
		else if (shop == 4) {

			if (staple_count >= B_upgrade_cost) {
				boss_upgrader(staple_count, cUpgrade2, B_upgrade_cost);
				system("cls");
				cout << endl << endl << endl << endl << endl;
				cout << endl << "Upgrade Purchased!" << endl << endl;
				cout << "\tEach Boss is now bossier! Coworkers are more efficient!" << endl;
				cout << endl << endl << "[Press 1] to return to UPGRADE SHOP." << endl;
				cout << "[Press 0] to continue mashing!" << endl;
				cin >> shop;
				b = 1;
			}
			else {
				cout << "You can't afford this!" << endl << endl << endl;
				cout << "Press 0 to leave the shop" << endl;
				cin >> shop;
				system("cls");
				cout << endl << endl << endl << endl << endl;
			}
		}

		// NEW BRANCH UPGRADE PURCHASE: 
		else if (shop == 5) {
			if (staple_count >= NB_upgrade_cost + 6) { // if this is not exactly NB_upgrade_cost due to math then it will be skipped
				new_branch_multiplier(ptr_NB_Upgrade4, ptr_NB_upgrade_cost, ptr_staple_count, ptr_cUpgrade2, ptr_bUpgrade3);
				system("cls");
				cout << endl << endl << endl << endl << endl;
				cout << "Congratulations you have become the CEO for a new branch!" << endl;
				cout << "You now have " << *ptr_cUpgrade2 << " coworkers and have a new boss for the new Branch!" << endl;
				cout << endl << endl << "[Press 1] to return to UPGRADE SHOP." << endl;
				cout << "[Press 0] to continue mashing!" << endl;
				cin >> shop;
				n = 1;
			}

			else {
				cout << "You can't afford this!" << endl << endl << endl;
				cout << "Press 0 to leave the shop" << endl;
				cin >> shop;
				system("cls");
				cout << endl << endl << endl << endl << endl;
			}
		}
		else if (NB_Upgrade4 >= 10) {
			system("cls");
			cout << "Congratulations, " << player_Name << "! You have now bought out every major competetor in the " << business_goal << " market!" << endl;
			cout << business_name << " is now one of the most successful " << business_goal << " businesses in the United States!";
			cout << "Your success story goes on to become a classroom classic in economics courses far and wide." << endl;
			cout << endl << endl << endl << endl;
			cout << "Just to think, all you had at one time was one stapler and a dream." << endl;
			cout << endl << endl;
			cout << "Thank you for playing Staple Masher." << endl << endl;
			cout << "Brought to you by: **** The Staple Masher Development Team ****" << endl;
			cout << "\t\t\t\tRiley Grace" << endl << "\t\t\t\tSeth Gibbs" << endl;
			cout << "\t\t\t\tAbdallah Mohamed" << endl << "\t\t\t\tand Karis Land" << endl << endl;
			cout << "\t\t\t\tNever stop chasing your dreams!" << endl; // Karis Land
		}

		//OLD LOCATION OF ELSE

	};
	return 0;
}



// MAIN GAME VARIABLES
//char enter = '\0'; // stores the enter character - '\n'
//double staple_count = -1; // stores the staple count // used in all upgrades deducted by cost
//double* ptr_staple_count = &staple_count; // use with upgrade functions to subtract cost from staple count

void stapler_counter(double* ptr_staple_count, double* ptr_sUpgrade1, double* ptr_cUpgrade2,
	double* ptr_bUpgrade3, double* ptr_NB_Upgrade4) {
	*ptr_staple_count = (*ptr_staple_count + 1) + ((*ptr_sUpgrade1) * (*ptr_cUpgrade2)) + (*ptr_bUpgrade3) + (*ptr_NB_Upgrade4);
} // Karis Land


// STAPLER UPGRADE VARIABLES:
//double sUpgrade1 = 1; // stores staple upgrade level
//double* ptr_sUpgrade1 = &sUpgrade1;
//double S_upgrade_cost = 100; // stores staple upgrade cost level 
//double* ptr_S_upgrade_cost = &S_upgrade_cost;

void stapler_upgrader(double* sUpgrade1, double* S_upgrade_cost, double* staple_count) {
	if (*staple_count >= *S_upgrade_cost) { // Seth Gibbs edit: SAFEGUARD prevents purchase when not enough staples
		*staple_count = (*staple_count) - (*S_upgrade_cost); // DEDUCTS UPGRADE COST FROM STAPLE COUNT
		*sUpgrade1 = (*sUpgrade1) + 1; // INCREASES UPGRADE LEVEL
		*S_upgrade_cost = (*S_upgrade_cost) + 500; // COST INCREASES EACH ITERATION
	}
} // Karis Land


// COWORKER UPGRADE VARIABLES: 
//double cUpgrade2 = 1; // stores coworker upgrade //Sets the value the coworker will add initally 
//double* ptr_cUpgrade2 = &cUpgrade2;
//double C_upgrade_cost = 500; // stores cost of coworker upgrade
//double* ptr_C_upgrade_cost = &C_upgrade_cost;

void coworker_upgrader(double* cUpgrade2, double* C_upgrade_cost, double* staple_count) {
	if (*staple_count >= *C_upgrade_cost) {
		*staple_count = (*staple_count) - (*C_upgrade_cost);
		*cUpgrade2 = (*cUpgrade2) + 2;
		*C_upgrade_cost = (*C_upgrade_cost) + 1000;
	}
} //Logan Tetrick TO DO: Shop entry 


// BOSS UPGRADE VARIABLES:
//double bUpgrade3 = 0;
//double* ptr_bUpgrade3 = &bUpgrade3;
//double B_upgrade_cost = 1000;
//double* ptr_B_upgrade_cost = &B_upgrade_cost;

void boss_upgrader(double& staple_count, double& cUpgrade2, double& B_upgrade_cost) {
	staple_count -= 1000;
	cUpgrade2 += 2;
	B_upgrade_cost = B_upgrade_cost + 1500;
}

// NEW BRANCH UPGRADE VARIABLES: 
//double NB_Upgrade4 = 0;
//double* ptr_NB_Upgrade4 = &NB_Upgrade4;
//double NB_upgrade_cost = 3000;
//double* ptr_NB_upgrade_cost = &ptr_NB_upgrade_cost;

void new_branch_multiplier(double* ptr_NB_Upgrade4, double* ptr_NB_upgrade_cost, double* staple_count, double* ptr_cUpgrade2, double* ptr_bUpgrade3) {
	if (*staple_count >= *ptr_NB_upgrade_cost) {
		*staple_count = (*staple_count) - (*ptr_NB_upgrade_cost);
		*ptr_NB_Upgrade4 = ((*ptr_NB_Upgrade4) + 1);
		*ptr_NB_upgrade_cost = (*ptr_NB_upgrade_cost) + 3500;
		(*ptr_cUpgrade2)++;
		(*ptr_bUpgrade3)++; // new boss added 
	}
}

