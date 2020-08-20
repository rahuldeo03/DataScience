{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Program to check if a number is divisible by 3 or 5 or both\n",
      "Enter the number: 2\n",
      "Not divisible by 3 or 5\n",
      "program completes\n"
     ]
    }
   ],
   "source": [
    "print(\"Program to check if a number is divisible by 3 or 5 or both\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number: 56\n",
      "Not divisible by 3 or 5\n",
      "program completes\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    num1 = int(input('Enter the number: '))\n",
    "    # Implement Logic and print result\n",
    "    if num1 % 3 == 0:\n",
    "        if num1 % 5 == 0:\n",
    "            print(\"Zoom-multiple of both.\")\n",
    "        else:\n",
    "            print(\"Zip-multiple of three.\")\n",
    "    elif num1 % 5 == 0:\n",
    "        print(\"Zap-multiple of five.\")\n",
    "    else:\n",
    "        print(\"Not divisible by 3 or 5\")\n",
    "except:\n",
    "    print(\"Something went wrong\")\n",
    "finally:\n",
    "    print('program completes')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
